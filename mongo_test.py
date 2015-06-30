from pymongo import MongoClient, ReturnDocument
import unittest

class TestTrivialMongoStuff(unittest.TestCase):
    def setUp(self):
        self.mongo = MongoClient('localhost', 27017)
        self.collection = self.mongo['data']['data']

    def test_mongo_insert(self):
        self.collection.insert({'value': 'data'})
        self.assertEquals('data', self.collection.find_one()['value'])

if __name__ == '__main__':
    unittest.main()
