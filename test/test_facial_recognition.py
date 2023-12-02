import unittest
from unittest.mock import patch
from facial_recognition import FacialRecognition

class TestFacialRecognition(unittest.TestCase):

    def setUp(self):
        self.facial_recognition = FacialRecognition()

    def test_initial_known_faces(self):
        # Test the initial state of known faces
        self.assertEqual(len(self.facial_recognition.known_faces), 20)

    def test_add_face_success(self):
        # Test adding a new face successfully
        result = self.facial_recognition.add_face("Person 21")
        self.assertTrue(result)
        self.assertIn("face_21", self.facial_recognition.known_faces)

    def test_add_face_failure(self):
        # Test failure when trying to add more than the maximum number of faces
        for i in range(22, FacialRecognition.MAX_FACES + 2):
            self.facial_recognition.add_face(f"Person {i}")
        result = self.facial_recognition.add_face("Person Overflow")
        self.assertFalse(result)
        self.assertNotIn("face_51", self.facial_recognition.known_faces)

    def test_identify_face(self):
        # Test the face identification method
        with patch('random.choices', return_value=['face_1']):
            identified_face = self.facial_recognition.identify_face()
            self.assertIn(identified_face, self.facial_recognition.known_faces)

    def test_is_known_face(self):
        # Test checking if a face is known
        self.assertTrue(self.facial_recognition.is_known_face("face_1"))
        self.assertFalse(self.facial_recognition.is_known_face("face_unknown"))

    def test_remove_face_success(self):
        # Test successful removal of a face
        result = self.facial_recognition.remove_face("face_1")
        self.assertTrue(result)
        self.assertNotIn("face_1", self.facial_recognition.known_faces)

    def test_remove_face_failure(self):
        # Test failure to remove a face that does not exist
        result = self.facial_recognition.remove_face("face_unknown")
        self.assertFalse(result)
