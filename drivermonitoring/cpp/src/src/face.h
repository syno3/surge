#pragma once

#ifndef FACE_H
#define FACE_H
#include <iostream>
#include <fstream>
#include <opencv2/opencv.hpp>
#include <opencv2/dnn/dnn.hpp>
#include <opencv2/dnn/all_layers.hpp>
#include <fstream>

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
    const std::string weights = "E:\surge\drivermonitoring\cpp\src\src\resources\frozen_inference_graph.pb";
    const std::string classes = "E:\surge\drivermonitoring\cpp\src\src\resources\object_detection_classes_coco.txt";
    const std::string config = "E:\surge\drivermonitoring\cpp\src\src\resources\ssd_mobilenet_v2_coco_2018_03_29.pbtxt.txt";

    std::vector<std::string> class_names;
    float min_confidence_score = 0.5;


    //void FaceDetector();
    void object_detection(const cv::Mat& frame);
    distance_to_camera_R distance_to_camera(const cv::Mat& frame);
    driver_attention_R driver_attention(const cv::Mat& frame);
    head_pose_R head_pose(const cv::Mat& frame);

};

#endif
