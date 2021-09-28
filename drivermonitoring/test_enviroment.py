import unittest
import pytest
from enviroment import enviroment
from main import videoOutput



class TestStringMethods(unittest.TestCase):
    
    # check import errors
    def test_import_error(self):
        try:
            from enviroment import enviroment
        except ImportError:
            self.fail("cannot import module")

    # we check if the path is empty
    def test_empty_path(self):
        path = videoOutput()
        path = path.path
        assert path != []

    # check if the output is not empty
    def test_brightness_str(self):
        path = enviroment()
        string = path.brightness_level
        assert string != ''

    #check if saturation output not empty
    def test_saturation_str(self):
        path = enviroment()
        string = path.saturation_level
        assert string !=''

    #check frames per second is not empty
    def test_frames_per_second_int(self):
        path = enviroment()
        output = path.frames_per_second
        assert output != 0

if __name__ == '__main__':
    unittest.main()