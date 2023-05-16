import cv2

from face_recognizer import DeepFaceRecognizer

image1 = cv2.imread(".face_db/Minh/1.jpg")
image2 = cv2.imread("./face_db/Trinh/2.jpg")


recognizer = DeepFaceRecognizer()


resp = recognizer.find([image1, image2])
name = recognizer.get_identity_names(resp)

print(name)