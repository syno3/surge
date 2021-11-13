#include "calibration.h"

/// we perform camera calibration in cpp
/// we dont have images
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
        success = cv::findChessboardCorners(gray, cv::Size(CHESSBOARD[0], CHESSBOARD[1]), corner_pts, CALIB_CB_ADAPTIVE_THRESH + CALIB_CB_NORMALIZE_IMAGE + CALIB_CB_FAST_CHECK);
        if (success) {
            cv::cornerSubPix(gray, corner_pts, Size(11, 11), Size(-1, -1),TermCriteria(TermCriteria::MAX_ITER | TermCriteria::EPS, 30, 0.001));
            cv::drawChessboardCorners(board, cv::Size(CHESSBOARD[0], CHESSBOARD[1]), corner_pts, success); // we draw the chessboard points
            objpoints.push_back(objp);
            imgpoints.push_back(corner_pts);
        }  
        cv::imshow("Image", board);
        cv::waitKey(0);
    }

};
void calibration::undistort(Mat& frame) {

};

// the debug function
void main() {
    calibration calibration; // class declaration
    const std::string path = "E:\\surge\\resources\\video1.mp4"; // will use to play video
    calibration.distortionCoeffiecient(); // we test the calibration
    cv::VideoCapture cap(path);
    cv::Mat frame;
    while (true) {
        cap.read(frame);
        resize(frame, frame, cv::Size(640, 480));
        imshow("video", frame);
        cv::waitKey(1);
    };
}

