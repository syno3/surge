// enviroment file
// main class
    // check brightness level
    // check saturation level
    // get frames per second (done)

#include "enviroment.h";

saturation_R enviroment::saturation_level(Mat frame){
    // we calculate the mean of hsv[...,2]
    // returns two variables(string , float value)
    cvtColor(frame, hsvImage, COLOR_BGR2HSV);
    const auto value_S = cv::mean(hsvImage);
    if(value_S[1] == enviroment::_no_saturation){
        return { "no saturation", (float)value_S[1] };
    }
    else if(value_S[1] > enviroment::_no_saturation && value_S[1] < enviroment::_little_saturation){
        return { "Minimal saturation", (float)value_S[1] };
    }
    else if(value_S[1] > enviroment::_little_saturation && value_S[1] < enviroment::_slight_saturation){
        return {"slight saturation", (float)value_S[1]};
    }
    else if(value_S[1] > enviroment::_slight_saturation && value_S[1] < enviroment::_normal_saturation){
        return { "normal saturation", (float)value_S[1] };
    }
    else (value_S[1] > enviroment::_normal_saturation); {
        return {"over saturation", (float)value_S[1]};
    }
};

brightness_R enviroment::brightness_level(Mat frame) {
    // we calculate the mean of hsv[...,1]
    // returns two variables(string , float value)
    cvtColor(frame, hsvImage, COLOR_BGR2HSV);
    const auto value = cv::mean(hsvImage);
    if (value[2] == enviroment::_no_exposure) {
        return {"no exposure", (float)value[2]};
    }
    else if (value[2] > enviroment::_no_exposure && value[2] < enviroment::_little_exposure) {
        return {"Minimal exposure", (float)value[2]};
    }
    else if (value[2] > enviroment::_little_exposure && value[2] < enviroment::_slight_exposure) {
        return {"slight exposure", (float)value[2]};
    }
    else if (value[2] > enviroment::_slight_exposure && value[2] < enviroment::_normal_exposure) {
        return {"normal exposure", (float)value[2]};
    }
    else (value[2] > enviroment::_normal_exposure); {
        return {"over exposure", (float)value[2]};
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
       cout << env.saturation_level(frame).value << endl;
       imshow("video", frame);
       waitKey(1);
   };
}