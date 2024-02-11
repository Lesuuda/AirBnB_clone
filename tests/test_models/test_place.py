import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.place import Place

class TestPlace(unittest.TestCase):

    def test_inheritance(self):
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertIsInstance(place, BaseModel)

    def test_id_generation(self):
        place1 = Place()
        place2 = Place()
        self.assertNotEqual(place1.id, place2.id)

    def test_created_updated_at(self):
        place = Place()
        self.assertIsInstance(place.created_at, datetime)
        self.assertIsInstance(place.updated_at, datetime)
        self.assertNotEqual(place.created_at, place.updated_at)

    def test_to_dict_method(self):
        place = Place()
        place_dict = place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertIn('id', place_dict)
        self.assertIn('__class__', place_dict)
        self.assertIn('created_at', place_dict)
        self.assertIn('updated_at', place_dict)
        
if __name__ == '__main__':
    unittest.main()
