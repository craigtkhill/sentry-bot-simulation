import unittest
from sensor import SensorProcessor

class TestSensor(unittest.TestCase):
    def setUp(self):
        self.sensor = SensorProcessor()
