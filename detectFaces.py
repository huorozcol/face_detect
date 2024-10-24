import cv2
import face_recognition


class Detect:
    def detectFaces(self, frame):
        #print('frame en detect: ', frame)
        frame = cv2.resize(frame,(400,400))
        if len(face_recognition.face_locations(frame)) > 0:

            face_loc = face_recognition.face_locations(frame)[0]
            print((face_recognition.face_locations(frame)))
            cv2.rectangle(frame, (face_loc[3],face_loc[0]),(face_loc[1],face_loc[2]), (0,255,0))
            cv2.imshow("image", frame)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            return
        else:
            print('No hay caras?',len(face_recognition.face_locations(frame)))
            return
#Detect.detectFaces(None,cv2.imread('./hugoorozco.jpeg'))