import math
import numpy as np
from numpy import dot
from numpy.linalg import norm

def get_direction(results, mp_pose):
    left = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].z
    right = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].z
    if left > right:
        return 'right'
    elif right >= left:
        return 'left'
    else:
        return 'none'

def get_pushup_ready(results, mp_pose, dir):
    if dir == 'right':
        # 준비 중인가? - 골반 - 발목 - 골반 정사영 각도
        right_hip = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP]  
        right_ankle = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE]

        right_ankle_visibility = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE].visibility

        degree = get_pro_degree(right_hip, right_ankle)

        if degree > 60 or right_ankle_visibility < 0.5:
            ready = 'notready'
        else:
            ready = 'ready'

        return ready
  
    elif dir == 'left':
        left_hip = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP]
        left_ankle = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ANKLE]

        left_ankle_visibility = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ANKLE].visibility

        degree = get_pro_degree(left_hip, left_ankle)

        if degree > 60 or left_ankle_visibility < 0.5:
            ready = 'notready'
        else:
            ready = 'ready'

        return ready


def get_pushup_status(results, mp_pose, dir):
    if dir == 'right':
        # # 손목 - 팔꿈치의 높이 차와 손목 - 어깨의 높이 차 비교    -   카메라 각도에 따라 차이가 심함
        # right_wrist = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].y
        # right_elbow = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].y
        # right_shoulder = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y

        # # 양수 값이 나오게 반대로 뺌
        # right_we = right_wrist - right_elbow
        # right_ws = right_wrist - right_shoulder

        # # 16, 19 -> 1.1875 / 29, 50 -> 1.7241  중간값 1.4558
        # right_ratio = right_ws / right_we

        # if right_ratio > 1.2558:
        #     status = 'up'
        # else:
        #     status = 'down'
        
        # return status, right_ratio

        
        
        # 손목 - 팔꿈치 - 어깨의 각도 
        right_wrist = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST]
        right_elbow = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW]
        right_shoulder = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER]

        right_degree = get_degree(right_wrist, right_elbow, right_shoulder)

        if right_degree > 130:
            status = 'up'
        else:
            status = 'down'

        return status, right_degree

    elif dir == 'left':
        # left_wrist = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].y
        # left_elbow = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].y
        # left_shoulder = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y

        # left_we = left_elbow - left_wrist
        # left_ws = left_shoulder - left_wrist

        # left_ratio = left_ws / left_we

        # if left_ratio > 1.4558:
        #     status = 'up'
        # else:
        #     status = 'down'
        
        # return status, left_ratio


        left_wrist = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST]
        left_elbow = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW]
        left_shoulder = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]

        left_degree = get_degree(left_wrist, left_elbow, left_shoulder)

        if left_degree > 130:
            status = 'up'
        else:
            status = 'down'

        return status, left_degree




def get_degree(A, B, C):
    v1 = (A.x - B.x, A.y - B.y, A.z - B.z)
    v2 = (C.x - B.x, C.y - B.y, C.z - B.z)
    cosin = dot(v1, v2)/(norm(v1)*norm(v2))
    degree = math.degrees(math.acos(cosin))
    return degree

def get_pro_degree(A, B):
    v1 = (A.x - B.x, A.y - B.y, A.z - B.z)
    v2 = (A.x - B.x, 0, A.z - B.z)
    cosin = dot(v1, v2)/(norm(v1)*norm(v2))
    degree = math.degrees(math.acos(cosin))
    return degree




###############################################
# def get_angles(results, mp_pose):
#     try:
#         angles = []

#         left_elbow = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW]
#         right_elbow = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW]

#         left_shoulder = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]
#         right_shoulder = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER]

#         left_hip = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP]
#         right_hip = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP]

#         left_wrist = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST]
#         right_wrist = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST]

#         left_knee = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE]
#         right_knee = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE]

#         left_ankle = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ANKLE]
#         right_ankle = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE]


#         left_shoulder_angle = get_degree(left_elbow, left_shoulder, left_hip)
#         right_shoulder_angle = get_degree(right_elbow, right_shoulder, right_hip)

#         left_elbow_angle = get_degree(left_wrist, left_elbow, left_shoulder)
#         right_elbow_angle = get_degree(right_wrist, right_elbow, right_shoulder)

#         left_hip_angle = get_degree(left_shoulder, left_hip, left_knee)
#         right_hip_angle = get_degree(right_shoulder, right_hip, right_knee)

#         left_knee_angle = get_degree(left_hip, left_knee, left_ankle)
#         right_knee_angle = get_degree(right_hip, right_knee, right_ankle)

#         angles = [left_shoulder_angle, right_shoulder_angle, left_elbow_angle, right_elbow_angle, left_hip_angle, right_hip_angle, left_knee_angle, right_knee_angle]
#         return angles
#     except:
#         pass

# def get_degree(A, B, C):
#     v1 = (A.x - B.x, A.y - B.y, A.z - B.z)
#     v2 = (C.x - B.x, C.y - B.y, C.z - B.z)
#     cosin = dot(v1, v2)/(norm(v1)*norm(v2))
#     degree = math.degrees(math.acos(cosin))
#     return degree

# def angle2text(angles):
#     return [f'shoulder:{round(angles[0])},{round(angles[1])}', f'elbow:{round(angles[2])},{round(angles[3])}',
#             f'hip:{round(angles[4])},{round(angles[5])}', f'knee:{round(angles[6])},{round(angles[7])}']