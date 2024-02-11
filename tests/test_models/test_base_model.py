#!/usr/bin/python3
"""
Tests for the BaseModel class
"""


import unittest
import os
from models.base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """unittests for the base class"""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_creation_of_instance(self):
        obj = BaseModel()
        obj1 = BaseModel()
        self.assertNotEqual(obj.id, obj1.id)
        self.assertIsInstance(obj.id, str)
        self.assertIsNotNone(obj.id)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_str_representation(self):
        obj = BaseModel()
        string_repr = str(obj)
        self.assertIn(type(obj).__name__, string_repr)
        self.assertIn(obj.id, string_repr)
        self.assertIn(str(obj.__dict__), string_repr)

    def test_save_method(self):
        obj = BaseModel()
        original_update = obj.updated_at
        obj.save()
        self.assertNotEqual(original_update, obj.updated_at)

    def test_to_dict(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['__class__'], type(obj).__name__)
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())
