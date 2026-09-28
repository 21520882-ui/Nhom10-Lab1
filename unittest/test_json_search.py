# Fill the Python code in this file
import unittest
from recursive_json_search import *
from test_data import *
from policy import POLICY

class json_search_test(unittest.TestCase):
    '''test     module      to      test        search      function        in      `recursive_json_search.py`'''
    def test_search_found(self):
        '''key should be found, return list should not be empty'''
        self.assertTrue([]!=json_search(key1, data, role="viewer"))
    def test_search_not_found(self):
        '''key should not be found, should return an empty list'''
        self.assertTrue([]==json_search(key2, data, role="admin"))
    def test_is_a_list(self):
        '''Should return a list'''
        self.assertIsInstance(json_search(key1, data, role="admin"), list)
    def test_wrong_role_cannot_read_secret(self):
        '''role khong co quyen khong duoc phep doc apikey'''
        result = json_search("apiKey", data, role="viewer")
        self.assertEqual([], result)
    def test_missing_role(self):
        '''khong cung cap role phai tra ve rong'''
        result = json_search("issueSummary", data)
        self.assertEqual([], result)
    def test_authorized_role(self):
        '''role hop le duoc phep doc du lieu'''
        self.assertTrue([]!=json_search("apiKey", data, role="admin"))
        
if __name__ == '__main__':
    unittest.main()
