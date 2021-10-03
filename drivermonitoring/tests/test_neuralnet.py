import unittest
import pytest
import sys
sys.path.append("..") # added for relative imports!
from neuralnet import *



class TestStringMethods(unittest.TestCase):

    def test_relative_import_error(self):
        try:
            from neuralnet import denseLayer
        except ImportError:
            self.fail("relative import error")

    def test_int_denselayer_inputs(self):
        # we check if error raised
        with self.assertRaises(TypeError):
            denseLayer('3', '4') # str

        with self.assertRaises(TypeError):
            denseLayer(3.03, 4.03) # float

        with self.assertRaises(TypeError):
            denseLayer('3', 4) # str + float

        with self.assertRaises(AssertionError):
            denseLayer(0, 0) # zero input

if __name__ == '__main__':
    unittest.main()
