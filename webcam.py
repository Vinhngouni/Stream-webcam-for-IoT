import cv2
from datetime import datetime

class Webcam():
    def __init__(self):
        self.vid = cv2.VideoCapture(0)
        # self.vid = cv2.VideoCapture(r"C:\Users\VINH-KMOU\OneDrive - g.kmou.ac.kr\1 - Research Paper\3 - Reach Stacker Assistance\Dataset\Video\Brief_Video.mp4")
    

    def get_frame(self):

        if not self.vid.isOpened():
            return

        while True:
            _, img = self.vid.read()
            self.vid.set(cv2.CAP_PROP_BUFFERSIZE, 10)
            height, width = img.shape[:2]
            # font
            font = cv2.FONT_HERSHEY_SIMPLEX
            org = (width-350, height-20)
            fontScale = 0.8
            color = (255, 255, 255)
            thickness = 2

            img = cv2.putText(img, datetime.now().strftime("%a %Y-%m-%d %H:%M:%S"), org, font,
                              fontScale, color, thickness, cv2.LINE_AA)

            yield cv2.imencode('.jpg', img)[1].tobytes()#frame 

       