#!/usr/bin/python3
""" base.py test cases """


import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """ test cases for Base """

    def test_id_none(self):
        b1 = Base()
        self.assertEqual(1, b1.id)

    def test_id(self):
        b2 = Base(12)
        self.assertEqual(12, b2.id)
