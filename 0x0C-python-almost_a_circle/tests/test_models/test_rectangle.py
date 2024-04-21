#!/usr/bin/python3
""" Rectangle test cases """
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """ Rectangle class test """
    def test_rectangle_nonId(self):
        """ testing none id """
        r1 = Rectangle(10, 2)
        self.assertEqual(1, r1.id)

    def test_rectangle_id(self):
        """ testing specific id """
        r2 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(12, r2.id)
        self.assertEqual(10, r2.width)
        self.assertEqual(2, r2.height)
        self.assertEqual(0, r2.x)
        self.assertEqual(0, r2.y)

    def test_area(self):
        """ testing area method """
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(56, r3.area())
