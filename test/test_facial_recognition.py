import unittest
from unittest.mock import patch
from facial_recognition import FacialRecognition

class TestFacialRecognition(unittest.TestCase):

    def setUp(self):
        self.facial_recognition = FacialRecognition()

    # Test Initialization
    def test_initialization(self):
        self.assertEqual(len(self.facial_recognition.known_faces), 20)
        self.assertIn('face_1', self.facial_recognition.known_faces)

    # Test Add Face
    def test_add_face(self):
        result = self.facial_recognition.add_face("Person 21")
        self.assertTrue(result)
        self.assertIn('face_21', self.facial_recognition.known_faces)

    # Test Add Face When Full
    def test_add_face_when_full(self):
        for i in range(21, 51):
            self.facial_recognition.add_face(f"Person {i}")

        result = self.facial_recognition.add_face("Person 51")
        self.assertFalse(result)

    # Test Identify Face
    def test_identify_face(self):
        with patch('random.choice', return_value='face_1'), \
             patch('random.randint', return_value=51):
            face_identified = self.facial_recognition.identify_face()
            self.assertIn(face_identified, ['face_1', 'face_51'])

    # Test Is Known Face
    def test_is_known_face(self):
        self.assertTrue(self.facial_recognition.is_known_face('face_1'))
        self.assertFalse(self.facial_recognition.is_known_face('face_51'))

    # Test Remove Face
    def test_remove_face(self):
        result = self.facial_recognition.remove_face('face_1')
        self.assertTrue(result)
        self.assertNotIn('face_1', self.facial_recognition.known_faces)

    # Test Remove Non-existent Face
    def test_remove_non_existent_face(self):
        result = self.facial_recognition.remove_face('face_51')
        self.assertFalse(result)

    # Additional tests can be added for edge cases and error conditions...

if __name__ == '__main__':
    unittest.main()
