import unittest
import pytest
from face import face

# global variables

class TestStringMethods(unittest.TestCase):

    # we check if harcaasacade path is empty
    def test_harcascaade_path_not_empty(self):
        Face = face()
        path = Face.front_face_harcascaade_path

        assert path !=[]

    # we check if detect face is bool
    def test_bool_detect_face(self):
        Face = face()
        output = Face.detect_face

        assert type(output) == bool





if __name__ == '__main__':
    unittest.main()