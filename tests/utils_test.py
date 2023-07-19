import unittest

from core.utils import validate_value


class UtilsTest(unittest.TestCase):
    def test_validate_value_success(self):
        self.assertTrue(validate_value('salam',str))
    def test_validate_value_failed(self):
        self.assertRaises(TypeError, validate_value,'salam',int)


