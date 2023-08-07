from flask import Flask, render_template, Response
from waitress import serve
from webcam import Webcam
app = Flask(__name__)

webcam = Webcam()


@app.route("/")
def index():
    return render_template("index.html")

def read_from_webcam():
    while True:
        # Read image from class Webcam
        image = next(webcam.get_frame())

        # Return to web by yield command
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + image + b'\r\n\r\n')


@app.route("/image_feed")
def image_feed():
    return Response( read_from_webcam(), mimetype="multipart/x-mixed-replace; boundary=frame" )

if __name__=="__main__":
    # app.run(host='0.0.0.0', debug=False)
    serve(app, host="0.0.0.0", port = 5000)