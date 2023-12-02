import random

class FacialRecognition:
    MAX_FACES = 50  # Maximum number of faces that can be stored

    def __init__(self):
        # Initialize with a predefined set of known faces
        self.known_faces = {f"face_{i}": f"Person {i}" for i in range(1, 21)}

    def add_face(self, face_data):
        # Add a new face to the known faces if the maximum limit is not reached
        if len(self.known_faces) < self.MAX_FACES:
            face_id = f"face_{len(self.known_faces) + 1}"  # Generate a new face ID
            self.known_faces[face_id] = face_data  # Add the new face
            return True  # Return True to indicate successful addition
        return False  # Return False if the maximum limit is reached

    def identify_face(self):
        # Randomly identify a face, with a bias towards known faces
        return random.choices(
            [random.choice(list(self.known_faces.keys())), f"face_{random.randint(1, self.MAX_FACES)}"],
            weights=[3, 1], k=1)[0]  # 3:1 ratio of choosing a known face over a random one

    def is_known_face(self, face_id):
        # Check if a face ID is in the list of known faces
        return face_id in self.known_faces

    def remove_face(self, face_id):
        # Remove a face from the known faces and return True if successful, False otherwise
        return self.known_faces.pop(face_id, False)  # False is returned if the face_id is not found