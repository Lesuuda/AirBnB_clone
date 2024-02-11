#!/usr/bin/python3

import unittest
import os
from models.engine.file_storage import FileStorage  # Replace 'your_module' with the actual module name
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_storage = FileStorage()

    def tearDown(self):
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_attributes(self):
        self.assertEqual(FileStorage._FileStorage__file_path, "file.json")
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)

    def test_all_method(self):
        result = self.file_storage.all()
        self.assertIsInstance(result, dict)
        self.assertEqual(result, FileStorage._FileStorage__objects)

    def test_new_method(self):
        # Test if new() method adds an object to __objects correctly
        test_instance = BaseModel()
        self.file_storage.new(test_instance)
        key = f"{test_instance.__class__.__name__}.{test_instance.id}"
        self.assertIn(key, FileStorage._FileStorage__objects)

    def test_save_method(self):
        # Test if save() method correctly serializes __objects to file
        test_instance = BaseModel()
        self.file_storage.new(test_instance)
        self.file_storage.save()
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

    def test_reload_method(self):
        # Test if reload() method correctly deserializes the file to __objects
        test_instance = BaseModel()
        self.file_storage.new(test_instance)
        self.file_storage.save()
        self.file_storage.reload()
        key = f"{test_instance.__class__.__name__}.{test_instance.id}"
        self.assertIn(key, FileStorage._FileStorage__objects)

    def test_reload_method_empty_file(self):
        # Test if reload() method handles an empty file gracefully
        # No exception should be raised
        empty_file_path = "empty_file.json"
        with open(empty_file_path, 'w') as empty_file:
            empty_file.write("")
        self.file_storage._FileStorage__file_path = empty_file_path
        self.file_storage.reload()
if __name__ == '__main__':
    unittest.main()
