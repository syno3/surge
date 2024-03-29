#pragma once

#ifndef CALIBRATION_h
#define CALIBRATION_h

#include <stdio.h>
#include <iostream>
#include <opencv2/opencv.hpp>
#include <opencv2/calib3d/calib3d.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>

using namespace cv;

class calibration {
public:
	// variable declaration
	std::vector<std::vector<cv::Point3f> > objpoints;
	std::vector<std::vector<cv::Point2f> > imgpoints;
	std::vector<cv::Point3f> objp;
	std::vector<cv::String> images;
	std::vector<cv::Point2f> corner_pts;
	std::string path = "./images/*.jpg";
	cv::Mat board, gray;
	bool success;

	int CHESSBOARD[2]{6, 9};

	//constructor declaration
	void distortionCoeffiecient();
	void undistort(Mat& frame);
};

#endif
