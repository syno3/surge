#include "face.h";

// function declaration
facedetect_R face::facedetect(cv::Mat frame) {

    return {};
};
distance_to_camera_R face::distance_to_camera(cv::Mat frame) {

    return {};
};
driver_attention_R face::driver_attention(cv::Mat frame) {

    return {};
};
objects_R face::objects(cv::Mat frame) {

    return {};
};
head_pose_R face::head_pose(cv::Mat frame) {

    return {};
};
body_pose_R face::body_pose(cv::Mat frame) {

    return {};
};

// the debug function
void main() {
    face face; // class declaration
    const std::string path = "E:\\surge\\resources\\video1.mp4";
    cv::VideoCapture cap(path);
    cv::Mat frame;
    while (true) {
        cap.read(frame);
        resize(frame, frame, cv::Size(), 0.5, 0.5);
        double fps = cap.get(cv::CAP_PROP_FPS);
        //cout << "Frames per second: " << fps << endl;
        //std::cout << face.body_pose(frame).value << std::endl;
        cv::imshow("video", frame);
        cv::waitKey(1);
    };
}