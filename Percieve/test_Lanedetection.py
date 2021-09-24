
# we write test functions for lane detection file
from Lanedetection import cameracalibration, Lanedetection
import unittest

class TestStringMethods(unittest.TestCase):

    def test_not_emptycornersfoun(self):
        """  
        we assert that the results from cameracalibration.cornersfound is not empty
        """
        
        with self.assertRaises(TypeError):
            objpoints, imgpoints = cameracalibration.cornersfound


    def test_not_empty_image(self):
        """ 
        we assert that the img variable from cameracalibration.cornersfound is not empty
        """
        assert 
        

    def test_ret_true(self):
        """ 
        we assert that the variable ret is true
        """
        assert True
        

    def test_distortion_coefficient_image(self):
        """ 
        we assert that the img from cameracalibration.distortionCoefficients is not None
        """
        assert True
        

    def test_pickle_dump_error(self):
        """ 
        we assert that theres no error in pickle dump
        """
        assert True

if __name__ == '__main__':
    unittest.main()

