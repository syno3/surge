 def number_detected_faces(self, frame: np.ndarray) -> int:

        """ 
        parameters
        _________

        Frame : we take the frames as the input

        function
        ________

        we use dlib.get_frontal_face_detector() to determine the coordiantes of faces in frames and count the number of coordinates.
        
        return
        _______

        int : number of detected faces in the image

        """
        detector = dlib.get_frontal_face_detector()
        frame = cv2.flip(frame, 1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)
        for _ in faces:
            i = i+1

        return i

    def driver_attention(self, frame: np.ndarray) ->bool:

        """ 
        parameters
        _________

        Frame : we take the frames as the input

        function
        ________

        
        return
        _______

        int : number of detected faces in the image

        """
        pass