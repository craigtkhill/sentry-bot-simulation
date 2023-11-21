import unittest
from config import Config

class TestConfig(unittest.TestCase):
    def setUp(self):
        self.config = Config()

    def test_set_area(self):
        self.config.set_area(5000)
        self.assertEqual(self.config.get_area(), 5000)
        self.config.set_area(10000)
        self.assertEqual(self.config.get_area(), 5000)
        self.config.set_area(-1000)
        self.assertEqual(self.config.get_area(), 0)