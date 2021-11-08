#include "calibration.h"

/// we perform camera calibration in cpp
void calibration::distortionCoeffiecient(){
	for (int i{ 0 }; i < CHESSBOARD[i]; i++) {
		for (int j{ 0 }; j < CHESSBOARD[j]; j++) {
			objp.emplace_back(cv::Point3f(j, i, 0));
		}
	}
    cv::glob(path, images);
    for (int i{ 0 }; i < images.size(); i++) {
        board = cv::imread(images[i]);
        cv::cvtColor(board, gray, cv::COLOR_BGR2GRAY);
        success = cv::findChessboardCorners(gray, cv::Size(CHESSBOARD[0], CHESSBOARD[1]), corner_pts, CV_CALIB_CB_ADAPTIVE_THRESH | CV_CALIB_CB_FAST_CHECK | CV_CALIB_CB_NORMALIZE_IMAGE);
        if (success) {
            cv::TermCriteria criteria(CV_TERMCRIT_EPS | CV_TERMCRIT_ITER, 30, 0.001);
            cv::cornerSubPix(gray, corner_pts, cv::Size(11, 11), cv::Size(-1, -1), criteria);
            objpoints.push_back(objp);
            imgpoints.push_back(corner_pts);
        }   
    }
    cv::Mat cameraMatrix, distCoeffs, R, T;
    cv::calibrateCamera(objpoints, imgpoints, cv::Size(gray.rows, gray.cols), cameraMatrix, distCoeffs, R, T);
    std::cout << "cameraMatrix : " << cameraMatrix << std::endl;
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

