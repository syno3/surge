#pragma once

#include <iostream>
#include <ctime>
#include <opencv2/opencv.hpp>
#include "opencv2/highgui/highgui.hpp"


using namespace cv;
using namespace std;

// enviroment class
class enviroment {
public:
    // exposure values
    const int _no_exposure = 0, _little_exposure = 65, _slight_exposure = 130, _normal_exposure = 194, _over_exposure = 255;
    //saturation values
    const int _no_saturation = 0, _little_saturation = 65, _slight_saturation = 130, _normal_saturation = 194, _over_saturation = 255;
    // frames per second values
    float prev_frame_time = 0.0, new_frame_time = 0.0;
    // Images
    Mat hsvImage;
    // constructors
    // brightness level constructor
    string brightness_level(Mat frame);
    string saturation_level(Mat frame);
};
// face class

class face {
public:
    // variable declaration

    // constructor declarations

};