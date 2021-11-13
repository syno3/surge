#define FACE_H
#include "face.h";
#define log(x) cout << x << endl
// function declaration

// we compute the eye aspect ratio
double compute_ear(std::vector<cv::Point>& vec) {
    return double();
};

// we perform actual sleep detection
driver_attention_R face::driver_attention(const cv::Mat& frame) {

    return driver_attention_R();
};
body_pose_R face::body_pose(const cv::Mat& frame) {
    // we determine the direction head is facing

    return body_pose_R();
};

// the debug function
void main() {
    //const std::string path = "E:\\surge\\resources\\video1.mp4"; // will use to play video
    VideoCapture cap(0);
    Mat frame;
    while (true) {
        cap.read(frame);
        auto start = getTickCount(); // we calculate clock cycles per second
        auto end = getTickCount();
        auto totalTime = (end - start) / getTickFrequency();
        log(totalTime);
        imshow("video", frame);
        waitKey(1);
    };
}
