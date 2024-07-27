"""python module"""

#!/usr/bin/python
import unittest
from parameterized import parameterized
from utils import access_nested_map

"""
TestAccessNestedMap class is a unit test class for the access_nested_map function.
Methods:
- test_access_nested_map: Test case for the access_nested_map function with different inputs.
Attributes:
- nested_map: A dictionary representing a nested map.
- path: A tuple representing the path to access a value in the nested map.
- expected: The expected output when accessing the value in the nested map using the given path.
"""

class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

if __name__ == "__main__":
    unittest.main()
