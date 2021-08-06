from Abstract.laneDetection import imagePreporcessing
import unittest

class TestimagePreporcessing(unittest.TestCase):
    
    def test_videopath(self):
        value = type(image.videopath('resource/video.mp4')) is str
        self.assertEqual(True, value)

if __name__ == '__main__':
    image = imagePreporcessing()
    unittest.main()
    