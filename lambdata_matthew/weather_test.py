from weather import *
import unittest
from unittest.mock import patch
import requests
import pandas as pd




class TestWeather(unittest.TestCase):
    """tests weather"""
    def test_init(self):
        self.assertEqual(Weather('322da9f437b1767029b90e4aa3da5a07', 42,-71)
        .response.ok,True)



if __name__ == '__main__':
    unittest.main()
