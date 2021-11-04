#pragma once


#include <iostream>
#include <opencv2/opencv.hpp>
#include "opencv2/highgui/highgui.hpp"


// return values for the face constructor functions
// face detect retrun values
struct facedetect_R {
    bool facedeteced;
    int count;
    int score;
    float x, w, y, h;
};
// distance from camera
struct distance_to_camera_R {
    float distance;
};
// driver attention return values
struct driver_attention_R {
    bool driversleeping;
};

// object detection return value
struct objects_R {
    int objscore;
    float ymin, xmin, ymax, xmax, pred_labels;
};
// head pose return values
struct head_pose_R {
    bool driverDistracted;
    std::string response_text;

};
// body pose return value
struct body_pose_R {
    float cx, cy;
};
// face class
class face {
public:
    // variable declaration

    // constructor declarations
    facedetect_R facedetect(cv::Mat frame);
    distance_to_camera_R distance_to_camera(cv::Mat frame);
    driver_attention_R driver_attention(cv::Mat frame);
    objects_R objects(cv::Mat frame);
    head_pose_R head_pose(cv::Mat frame);
    body_pose_R body_pose(cv::Mat frame);
};