#include "calibration.h"

/// we perform camera calibration in cpp
void calibration::distortionCoeffiecient(){
	for (int i{ 0 }; i < CHESSBOARD[i]; i++) {
		for (int j{ 0 }; j < CHESSBOARD[j]; j++) {
			objp.emplace_back(cv::Point3f(j, i, 0));
		}
	}


};

// the debug function
void main() {
    calibration calibration; // class declaration
    const std::string path = "E:\\surge\\resources\\video1.mp4"; // will use to play video
    cv::VideoCapture cap(path);
    cv::Mat frame;
    while (true) {
        cap.read(frame);
        resize(frame, frame, cv::Size(640, 480));
        imshow("video", frame);
        cv::waitKey(1);
    };
}

