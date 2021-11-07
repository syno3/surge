#pragma once

#ifndef FACE_H
#define FACE_H
#include <iostream>
#include <fstream>
#include <opencv2/opencv.hpp>
#include <opencv2/dnn/dnn.hpp>
#include <opencv2/dnn/all_layers.hpp>

// we add global type declaration

using namespace std;
using namespace cv;
using namespace dnn;

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
    const std::string classes = "E:\\surge\\drivermonitoring\\cpp\\src\\src\\assets\\ssd_mobilenet_v2_coco_2018_03_29.pbtxt";
    const std::string tensorflowConfigFile = "E:\\surge\\drivermonitoring\\cpp\\src\\src\\assets\\opencv_face_detector.pbtxt";
    const std::string tensorflowWeightFile = "E:\\surge\\drivermonitoring\\cpp\\src\\src\\assets\\opencv_face_detector_uint8.pb";


    std::vector<std::string> class_names;
    Net net;
    float min_confidence_score = 0.5;

    void FaceDetector();
    void face_detection(const cv::Mat frame);
    distance_to_camera_R distance_to_camera(const cv::Mat& frame);
    driver_attention_R driver_attention(const cv::Mat& frame);
    head_pose_R head_pose(const cv::Mat& frame);

};

#endif
