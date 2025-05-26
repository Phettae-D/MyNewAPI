# import cv2
# from cvzone.HandTrackingModule import HandDetector
# from flask import Flask, request, jsonify
# import socket

# HandTacking = Flask(__name__)

# @HandTacking.route('/Tacking-user', methods=['GET'])
# def Tacking_user():
#  w,h=1280,720
#  cap = cv2.VideoCapture(0)
#  cap.set(3,w)
#  cap.set(4,h)
#  detecter = HandDetector(maxHands=1,detectionCon=0.8)
#  soc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#  addressport = ("127.0.0.1",5052)
#  while True:
#     succcess, img =cap.read()
#     hands , img = detecter.findHands(cv2.flip(img,1))
#     ##hands , img = detecter.findHands(img)
#     data = []
#     if hands:
#         hand = hands[0]
#         lmList = hand['lmList']
#         for lm in lmList:
#             data.extend([lm[0],h-lm[1],lm[2]])
#             soc.sendto(str.encode(str(data)),addressport)
#     img = cv2.resize(img,(0,0),None,0.5,0.5)
#     cv2.imshow("cam",img)
#     cv2.waitKey(1)

# if __name__ == "__main__":
#     HandTacking.run(host='0.0.0.0')


import cv2
from cvzone.HandTrackingModule import HandDetector
from flask import Flask, request, jsonify
import socket

HandTacking = Flask(__name__)

@HandTacking.route('/', methods=['GET'])
def test():
    soc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    addressport = ("127.0.0.1",5052)
    soc.sendto(str.encode(str('data')),addressport)

@HandTacking.route('/Tacking-user', methods=['GET'])
def Tacking_user():
 w,h=1280,720
 cap = cv2.VideoCapture(0)
 cap.set(3,w)
 cap.set(4,h)
 detecter = HandDetector(maxHands=1,detectionCon=0.8)
 soc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
 addressport = ("127.0.0.1",5052)
 while True:
    succcess, img =cap.read()
    hands , img = detecter.findHands(cv2.flip(img,1))
    ##hands , img = detecter.findHands(img)
    data = []
    if hands:
        hand = hands[0]
        lmList = hand['lmList']
        for lm in lmList:
            data.extend([lm[0],h-lm[1],lm[2]])
            soc.sendto(str.encode(str(data)),addressport)
    img = cv2.resize(img,(0,0),None,0.5,0.5)
    cv2.imshow("cam",img)
    cv2.waitKey(1)

if __name__ == "__main__":
    HandTacking.run(host='0.0.0.0')

Tacking_user()
