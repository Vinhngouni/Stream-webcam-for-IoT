import cv2, datetime
from flask import Flask, Response
from waitress import serve

app = Flask(__name__)

def generate_frames():
    cap = cv2.VideoCapture(0)  # Open the webcam (0 is usually the default webcam index)

    while True:
        ret, frame = cap.read()  # Read a frame from the webcam

        if not ret:
            break
        height, width = frame.shape[:2]
        # font
        font = cv2.FONT_HERSHEY_SIMPLEX
        org = (width-360, height-20)
        fontScale = 0.8
        color = (255, 255, 255)
        thickness = 2

        frame = cv2.putText(frame, datetime.datetime.now().strftime("%a %Y-%m-%d %H:%M:%S"), org, font,
                            fontScale, color, thickness, cv2.LINE_AA)

        ret, buffer = cv2.imencode('.jpg', frame)  # Convert the frame to JPEG format
        if not ret:
            break

        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # Yield the frame as a response

    cap.release()

@app.route('/image_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port = 5000)
    # app.run(host='0.0.0.0', port=5000)
