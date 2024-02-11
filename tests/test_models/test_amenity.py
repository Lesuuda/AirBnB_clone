import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):

    def test_inheritance(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity, BaseModel)

    def test_attributes(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_attributes_types(self):
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)

    def test_id_generation(self):
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)

    def test_created_updated_at(self):
        amenity = Amenity()
        self.assertIsInstance(amenity.created_at, datetime)
        self.assertIsInstance(amenity.updated_at, datetime)
        self.assertNotEqual(amenity.created_at, amenity.updated_at)

    def test_to_dict_method(self):
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertIn('id', amenity_dict)
        self.assertIn('__class__', amenity_dict)
        self.assertIn('created_at', amenity_dict)
        self.assertIn('updated_at', amenity_dict)
       
if __name__ == '__main__':
    unittest.main()
