# facial_recognition.py

import random

class FacialRecognition:
    MAX_FACES = 50

    def __init__(self):
        self.known_faces = {f"face_{i}": f"Person {i}" for i in range(1, 21)}

    def add_face(self, face_data):
        if len(self.known_faces) < self.MAX_FACES:
            face_id = f"face_{len(self.known_faces) + 1}"
            self.known_faces[face_id] = face_data
            return True
        return False

    def identify_face(self):
        return random.choices(
            [random.choice(list(self.known_faces.keys())), f"face_{random.randint(1, self.MAX_FACES)}"],
            weights=[3, 1], k=1)[0]

    def is_known_face(self, face_id):
        return face_id in self.known_faces

    def remove_face(self, face_id):
        return self.known_faces.pop(face_id, False)
