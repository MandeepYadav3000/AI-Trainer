import cv2
import mediapipe as mp
import numpy as np
import matplotlib.pyplot as plt

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
counter = 0
stage = None


def calculate_angle(a, b, c):
    a = np.array(a)  # First
    b = np.array(b)  # Mid
    c = np.array(c)  # End

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180.0:
        angle = 360 - angle

    return angle

cap = cv2.VideoCapture(0)



with mp_pose.Pose(min_detection_confidence=0.9, min_tracking_confidence=0.9) as pose:
    while cap.isOpened():
        ret, frame = cap.read()


        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # image.flags.writeable = False

        results = pose.process(image)
        print(results)

        # image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

