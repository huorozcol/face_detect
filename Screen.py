from threading import Thread
from detectFaces import *

class ShowFrame:
    def __init__(self, frame):
        print('se instancia la clase')
        #self.showScreen(frame)


    def showScreen(self, frame):

        #cv2.imshow("Frame", frame)
        #cv2.waitKey(1)
        thre_detec = Thread(name='detect_faces', target=Detect.detectFaces, args=(None,frame,), daemon=True)
        thre_detec.start()
        return
