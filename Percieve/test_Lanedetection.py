
# we write test functions for lane detection file
from Lanedetection import CameraCalibration, LaneDetect
import unittest
from logging import error
import pickle


class TestStringMethods(unittest.TestCase):

    def test_not_emptycornersfound(self):

        """  
        we assert that the results from cameracalibration.cornersfound is not empty
        """

        try:
            cameracalibration = CameraCalibration(9, 6)
            objpoints, _ = cameracalibration.cornersfound

            if objpoints == []:
                self.fail('The objpoints list is empty')
        except TypeError:
            self.fail("test failed raised TypeError")

    def test_not_empty_image_(self):

        """ 
        we assert that the img variable from cameracalibration.cornersfound is not empty
        """

        cameracalibration = CameraCalibration(9, 6)
        images = cameracalibration.images

        if images == []:
            self.fail('The list of images are empty')

    def test_pickle_dump_error(self):
        """ 
        we assert that theres no error in pickle dump
        """
        try:
            cameracalibration = CameraCalibration(9, 6)
            with open(cameracalibration.path_calibrationPickle, "rb") as input_file:
                e = pickle.load(input_file)
        except EOFError:
            self.fail("Cannot load pickle file")

if __name__ == '__main__':
    unittest.main()

