
import unittest
import pytest
import sys
sys.path.append("..") # added for relative imports!


class TestStringMethods(unittest.TestCase):
    
    def __init__(self, *args, **kwargs):
        super(TestStringMethods, self).__init__(*args, **kwargs)

    # check import errors
    def test_import_error(self):
        try:
            from enviroment import enviroment
        except ImportError:
            self.fail("cannot import module")


if __name__ == '__main__':
    unittest.main()
