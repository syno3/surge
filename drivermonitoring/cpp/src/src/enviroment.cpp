// enviroment file
// main class
    // check brightness level
    // check saturation level
    // get frames per second

#include <iostream>
#include <ctime>
#include <opencv2/opencv.hpp>


using namespace cv;
using namespace std;

class enviroment {
public:
    // exposure values
    const int _no_exposure = 0, _little_exposure = 65, _slight_exposure = 130, _normal_exposure = 194, _over_exposure = 255;
    //saturation values
    const int _no_saturation = 0, _little_saturation = 65, _slight_saturation = 130, _normal_saturation = 194, _over_saturation = 255;
    // frames per second values
    const float prev_frame_time = 0.0, new_frame_time = 0.0;
    // constructors
    // brightness level constructor
    float brightness_level(Mat frame) {
        return 0.0;
    };
    // saturation level constructor
    float saturation_level(Mat frame) {
        return 0.0;
    };
    // frames per second constructor
    int frames_per_second() {
        return 0;
    };
};


int main() {
    enviroment env;
    std::cout << env._little_exposure << endl;
    return 0;
}
