#include "face.h";

// function declaration
// we try to write everything with computer vison and keras (if it works)

//we build face detection constructor
std::vector<cv::Rect> face::detect_face_rectangles(const cv::Mat& frame) {
    // we try something else
    std::vector<cv::Rect> faces;

    return faces;
};
distance_to_camera_R face::distance_to_camera(const cv::Mat& frame) {

    return distance_to_camera_R();
};
driver_attention_R face::driver_attention(const cv::Mat& frame) {

    return driver_attention_R();
};
head_pose_R face::head_pose(const cv::Mat& frame) {

    return head_pose_R();
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
        std::cout << "Frames per second: " << fps << std::endl;
        face.detect_face_rectangles(frame); // function call for face detection
        cv::imshow("video", frame);
        cv::waitKey(1);
    };
}
