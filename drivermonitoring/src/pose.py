import numpy as np
import cv2
import mediapipe as mp


class pose:
    print('hello there')
    def __init__(self):
         # mediapipe submodules
        self.mp_face_detection = mp.solutions.face_detection
        self.mp_drawing = mp.solutions.drawing_utils
        
        # mediapipe pose submodules
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose()
        self.mpDraw = mp.solutions.drawing_utils
        # head pose detection
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)
        self.distracted = False
        self.text = None
        
        #other values
        self.text = None
    # we perform head pose detection
    def head_pose(self, frame:np.ndarray) -> str:
        frame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
        frame.flags.writeable = False
        results = self.face_mesh.process(frame)
        frame.flags.writeable = True
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        
        img_h, img_w, img_c = frame.shape
        face_3d = []
        face_2d = []

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                for idx, lm in enumerate(face_landmarks.landmark):
                    if idx == 33 or idx == 263 or idx == 1 or idx == 61 or idx == 291 or idx == 199:
                        if idx == 1:
                            _ = (lm.x * img_w, lm.y * img_h)
                            _ = (lm.x * img_w, lm.y * img_h, lm.z * 8000)

                        x, y = int(lm.x * img_w), int(lm.y * img_h)

                        # Get the 2D Coordinates
                        face_2d.append([x, y])

                        # Get the 3D Coordinates
                        face_3d.append([x, y, lm.z])       

            # Convert it to the NumPy array
            face_2d = np.array(face_2d, dtype=np.float64)

            # Convert it to the NumPy array
            face_3d = np.array(face_3d, dtype=np.float64)
            # The camera matrix
            focal_length = 1 * img_w

            cam_matrix = np.array([ [focal_length, 0, img_h / 2],
                                    [0, focal_length, img_w / 2],
                                    [0, 0, 1]])

            # The Distance Matrix
            dist_matrix = np.zeros((4, 1), dtype=np.float64)

            # Solve PnP
            _, rot_vec, _ = cv2.solvePnP(face_3d, face_2d, cam_matrix, dist_matrix)

            # Get rotational matrix
            rmat, _ = cv2.Rodrigues(rot_vec)

            # Get angles
            angles, _, _, _, _, _ = cv2.RQDecomp3x3(rmat)

            # Get the y rotation degree
            x = angles[0] * 360
            y = angles[1] * 360
            
            if y < -10:
                self.text = "Left"
                self.distracted = True
            elif y > 10:
                self.text = "Right"
                self.distracted = True
            elif x < -10:
                self.text = "Down"
                self.distracted = True
            else:
                self.text = "Forward"
                self.distracted = False

        return self.distracted, self.text
    
    # we detect for proper pose in driving (aka both hands at steering wheel)
    def body_pose(self, frame:np.ndarray):
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.pose.process(imgRGB)
        if results.pose_landmarks:
            #self.mpDraw.draw_landmarks(frame, results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
            for _, lm in enumerate(results.pose_landmarks.landmark):
                h, w,_ = frame.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                
        return cx, cy
    