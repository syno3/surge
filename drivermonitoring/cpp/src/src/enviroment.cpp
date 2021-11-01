// enviroment file
// main class
    // check brightness level
    // check saturation level
    // get frames per second

#include "classes.h";

string enviroment::saturation_level(Mat frame){
    // we calculate the mean of hsv[...,2]
    cvtColor(frame, frame, COLOR_BGR2HSV);
    float value_S = (float)mean(frame)[1];
    if(value_S == enviroment::_no_saturation){
        return "no saturation";
    }
    else if(value_S > enviroment::_no_saturation && value_S < enviroment::_little_saturation){
        return "Minimal saturation";
    }
    else if(value_S > enviroment::_little_saturation && value_S < enviroment::_slight_saturation){
        return "slight saturation";
    }
    else if(value_S == enviroment::_slight_saturation && value_S < enviroment::_normal_saturation){
        return "normal saturation";
    }
    else (value_S == enviroment::_normal_saturation && value_S < enviroment::_over_saturation);{
        return "over saturation";
    }
};

string enviroment::brightness_level(Mat frame) {
    // we calculate the mean of hsv[...,1]
    cvtColor(frame, frame, COLOR_BGR2HSV);
    float value = (float)mean(frame)[2];
    if (value == enviroment::_no_exposure) {
        return "no saturation";
    }
    else if (value > enviroment::_no_exposure && value < enviroment::_little_exposure) {
        return "Minimal exposure";
    }
    else if (value > enviroment::_little_exposure && value < enviroment::_slight_exposure) {
        return "slight exposure";
    }
    else if (value == enviroment::_slight_exposure && value < enviroment::_normal_exposure) {
        return "normal exposure";
    }
    else (value == enviroment::_normal_exposure && value < enviroment::_over_exposure); {
        return "over exposure";
    }
};


// we debug the enviroment class
void main() {
   enviroment env; // class declaration
   const string path = "E:\\surge\\resources\\video1.mp4";
   VideoCapture cap(path);
   Mat frame;
   while (true) {
       cap.read(frame);
       resize(frame, frame, Size(), 0.5, 0.5);
       double fps = cap.get(CAP_PROP_FPS);
       cout << "Frames per second: " << fps << endl;
       imshow("video", frame);
       waitKey(1);
   };
}