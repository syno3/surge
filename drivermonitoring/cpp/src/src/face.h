#pragma once

#ifdef FACE_H
#define FACE_H
#include <iostream>
#include <opencv2/opencv.hpp>
#include <opencv2/highgui/highgui.hpp>

#include <dlib/opencv.h>
#include <dlib/image_processing/frontal_face_detector.h>
#include <dlib/image_processing/render_face_detections.h>
#include <dlib/image_processing.h>
#include <dlib/gui_widgets.h>
#include <dlib/image_io.h>




// we add global type declaration
using namespace dlib;
using namespace std;
using namespace cv;

// return values for the face constructor functions
// face detect retrun values
// driver attention return values
struct driver_attention_R {
    bool driversleeping;
};

// head pose return values
struct body_pose_R {
    bool driverDistracted;
    std::string response_text;

};
// face class
class face {
public:
    //class variables
    shape_predictor sp;
    std::vector<cv::Point> righteye;
    std::vector<cv::Point> lefteye;

    // constructor declarations
    double compute_ear(std::vector<cv::Point>& vec);
    driver_attention_R driver_attention(const cv::Mat& frame);
    body_pose_R body_pose(const cv::Mat& frame);

};

#endif
