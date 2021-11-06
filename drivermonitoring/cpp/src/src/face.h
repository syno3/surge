#pragma once


#include <iostream>
#include <opencv2/opencv.hpp>
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/objdetect.hpp"
#include <opencv2/dnn/dnn.hpp>

// we add global type declaration

// return values for the face constructor functions
// face detect retrun values
struct facedetect_R {
    bool facedeteced;
    int count;
    int score;
    float x, y, w, h;
};
// distance from camera
struct distance_to_camera_R {
    float distance;
};
// driver attention return values
struct driver_attention_R {
    bool driversleeping;
};

// head pose return values
struct head_pose_R {
    bool driverDistracted;
    std::string response_text;

};
// face class
class face {
public:
    // constructor declarations
    const std::string path = "E:\\surge\\drivermonitoring\\assets\\front_face.xml";
    cv::CascadeClassifier facecascade;
    std::vector<cv::Rect> faces;
    cv::Mat gray;

    //void FaceDetector();
    std::vector<cv::Rect> detect_face_rectangles(const cv::Mat& frame);
    distance_to_camera_R distance_to_camera(const cv::Mat& frame);
    driver_attention_R driver_attention(const cv::Mat& frame);
    head_pose_R head_pose(const cv::Mat& frame);

};
