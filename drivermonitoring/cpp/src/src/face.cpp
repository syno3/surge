#include "face.h";
#define log(x) cout << x << endl
// function declaration
// we try to write everything with computer vison and keras (if it works)

//we build face detection constructor
void face::FaceDetector() {
    ifstream ifs(classes.c_str());
    string line;
    while (getline(ifs, line))
    {
        //log(line);
        class_names.push_back(line);
    }
    net = cv::dnn::readNetFromTensorflow(tensorflowWeightFile, tensorflowConfigFile);

};

void face::face_detection(const cv::Mat frame) {
    Mat blob = blobFromImage(frame, 1.0, Size(300, 300), Scalar(127.5, 127.5, 127.5), true, false);
    net.setInput(blob, "data");
    Mat detection = net.forward("detection_out");
    Mat results(detection.size[2], detection.size[3], CV_32F, detection.ptr<float>());

    for (int i = 0; i < results.rows; i++) {
        int class_id = int(results.at<float>(i, 1));
        float confidence = results.at<float>(i, 2);

        // Check if the detection is over the min threshold and then draw bbox
        if (confidence > min_confidence_score) {
            int bboxX = int(results.at<float>(i, 3) * frame.cols);
            int bboxY = int(results.at<float>(i, 4) * frame.rows);
            int bboxWidth = int(results.at<float>(i, 5) * frame.cols - bboxX);
            int bboxHeight = int(results.at<float>(i, 6) * frame.rows - bboxY);
            rectangle(frame, Point(bboxX, bboxY), Point(bboxX + bboxWidth, bboxY + bboxHeight), Scalar(0, 0, 255), 2);
            string class_name = class_names[class_id - 1];
            putText(frame, class_name + " " + to_string(int(confidence * 100)) + "%", Point(bboxX, bboxY - 10), FONT_HERSHEY_SIMPLEX, 1.5, Scalar(0, 255, 0), 2);
        }
    }

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
    //const std::string path = "E:\\surge\\resources\\video1.mp4"; // will use to play video
    face.FaceDetector(); // setup function
    cv::VideoCapture cap(0);
    cv::Mat frame;
    while (true) {
        cap.read(frame);
        auto start = getTickCount(); // we calculate clock cycles per second
        face.face_detection(frame); // actual face detection
        auto end = getTickCount();
        auto totalTime = (end - start) / getTickFrequency();
        log(totalTime);
        cv::imshow("video", frame);
        cv::waitKey(1);
    };
}
