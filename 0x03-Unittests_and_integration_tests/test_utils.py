#!/usr/bin/env python3
"""
Testing Module for test_utils.py
"""
from parameterized import parameterized
import unittest
from unittest.mock import Mock, patch
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Test Suite for access_tested_map function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Asserts if the return value of access_nested_map matches
        the expected result
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(expected_result, result)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map, path, exception):
        """
        Asserts if the KeyError exception is raised
        """
        with self.assertRaises(KeyError) as key_error:
            access_nested_map(nested_map, path)
            self.assertEqual(exception, key_error.exception)


class TestGetJson(unittest.TestCase):
    """
    Test Suite for get_json function
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Asserts that the get_json function return value matches
        the expected result
        """
        mocked_response = Mock()
        mocked_response.json.return_value = test_payload

        with patch('requests.get', return_value=mocked_response):
            expected_response = get_json(test_url)
            self.assertEqual(expected_response, test_payload)
            mocked_response.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    """
    Test Suite for memoize function
    """
    def test_memoize(self):
        """
        Tests memoization of a function
        """
        class TestClass:
            """ Test Class """
            def a_method(self):
                """ Returns an integer, 42"""
                return 42

            @memoize
            def a_property(self):
                """ Returns a memoized property """
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock_memo:
            memo_test = TestClass()
            memo_test.a_property
            memo_test.a_property
            mock_memo.asset_called_once()
