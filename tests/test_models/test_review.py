import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.review import Review

class TestReview(unittest.TestCase):

    def test_inheritance(self):
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review, BaseModel)

    def test_created_updated_at(self):
        review = Review()
        self.assertIsInstance(review.created_at, datetime)
        self.assertIsInstance(review.updated_at, datetime)
        self.assertNotEqual(review.created_at, review.updated_at)

    def test_to_dict_method(self):
        review = Review()
        review_dict = review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertIn('id', review_dict)
        self.assertIn('__class__', review_dict)
        self.assertIn('created_at', review_dict)
        self.assertIn('updated_at', review_dict)

if __name__ == '__main__':
    unittest.main()
