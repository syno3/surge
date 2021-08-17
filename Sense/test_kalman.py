from unittest import TestCase
from kalman import KalmanFilter

class TestKalmanFilter(TestCase):
    def can_construct(self) -> bool:
        x = 0.2
        y = 0.3
        KF = KalmanFilter(initial_x=x, initial_y=y)
        
        return self.assertAlmostEqual(KF.x[0], x)