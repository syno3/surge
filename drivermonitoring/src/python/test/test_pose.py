# test for python pose
import unittest
import pytest
import sys
sys.path.append("..") # added for relative imports!

# global variables

class TestStringMethods(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestStringMethods, self).__init__(*args, **kwargs)

    # we test module error
    def test_module_import_erro(self, *args):
        try:
            from pose import pose
            self.pose = pose()

        except ImportError:
            self.fail("import Failed")

    # we test for missing libraries
    def test_missing_libraries(self, *args):
        try:
            import mediapipe
            import cv2
            import numpy
        except Exception as e:
            self.fail(e)
    
    

    # we test mediapipe



if __name__ == '__main__':
    unittest.main()