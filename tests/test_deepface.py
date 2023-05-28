import sys
 
# setting path
sys.path.append('../')
# print(sys.path)
import cv2

from face_recognizer import DeepFaceRecognizer

image1 = cv2.imread("F:/3rdYear/nhandang/face/face_surveillance/face_db/SongHyeKyo/26.jpg")
image2 = cv2.imread("F:/3rdYear/nhandang/face/face_surveillance/face_db/SongJoongKi/22.jpg")
image3 = cv2.imread("F:/3rdYear/nhandang/face/face_surveillance/face_db/SongJoongKi/23.jpg")

# image1 = cv2.imread("F:/3rdYear/nhandang/face/face_surveillance/Trinh/1.jpg")
# image2 = cv2.imread("F:/3rdYear/nhandang/face/face_surveillance/Trinh/3.jpg")

image4 = cv2.imread("F:/3rdYear/nhandang/face/face_surveillance/Trinh/1.jpg")


recognizer = DeepFaceRecognizer()


resp = recognizer.find([image1, image2, image3, image4])
name = recognizer.get_identity_names(resp)

print(name)