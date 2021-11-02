// enviroment file
// main class
    // check brightness level (more bugs)
    // check saturation level (some bugs)
    // get frames per second (done)

#include "enviroment.h";

saturation_R enviroment::saturation_level(Mat frame){
    // we calculate the mean of hsv[...,2]
    // returns two variables(string , float value)
    cvtColor(frame, hsvImage, COLOR_BGR2HSV);
    float value_S = (float)mean(hsvImage)[1];
    if(value_S == enviroment::_no_saturation){
        return { "no saturation", value_S };
    }
    else if(value_S > enviroment::_no_saturation && value_S < enviroment::_little_saturation){
        return { "Minimal saturation", value_S };
    }
    else if(value_S > enviroment::_little_saturation && value_S < enviroment::_slight_saturation){
        return { "slight saturation", value_S };
    }
    else if(value_S == enviroment::_slight_saturation && value_S < enviroment::_normal_saturation){
        return { "normal saturation", value_S };
    }
    else (value_S == enviroment::_normal_saturation && value_S < enviroment::_over_saturation);{
        return { "over saturation", value_S };
    }
};

brightness_R enviroment::brightness_level(Mat frame) {
    // we calculate the mean of hsv[...,1]
    // returns two variables(string , float value)
    cvtColor(frame, hsvImage, COLOR_BGR2HSV);
    float value = (float)mean(hsvImage)[2];
    if (value == enviroment::_no_exposure) {
        return { "no saturation", value };
    }
    else if (value > enviroment::_no_exposure && value < enviroment::_little_exposure) {
        return {"Minimal exposure", value};
    }
    else if (value > enviroment::_little_exposure && value < enviroment::_slight_exposure) {
        return {"slight exposure", value};
    }
    else if (value == enviroment::_slight_exposure && value < enviroment::_normal_exposure) {
        return {"normal exposure", value};
    }
    else (value == enviroment::_normal_exposure && value < enviroment::_over_exposure); {
        return {"over exposure", value};
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
       //cout << "Frames per second: " << fps << endl;
       cout << env.brightness_level(frame).value << endl;
       imshow("video", frame);
       waitKey(1);
   };
}