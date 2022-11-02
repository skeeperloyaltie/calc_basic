#!/usr/bin/python3
"""Defines unittests for area_perimeter.py"""


import pep8
import unittest
import inspect
import area_perimeter
from area_perimeter import Object


class TestObjectDocs(unittest.TestCase):
    """ checking documentation and pep8 style"""
    @classmethod
    def setUpClass(cls):
        """setup for documentation tests"""
        cls.base_func = inspect.getmembers(Object, inspect.isfunction)

    def test_pep8_style_Object(self):
        """Test that area_perimeter.py meets PEP8 style."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['area_perimeter.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_style_unittest(self):
        """Test that test_area_perimeter.py meets PEP8 style."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_area_perimeter.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Tests for the module docstring"""
        self.assertTrue(len(area_perimeter.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the Object class docstring"""
        self.assertTrue(len(Object.__doc__) >= 1)
