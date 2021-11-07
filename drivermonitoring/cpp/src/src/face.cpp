#include "face.h";

// function declaration
// we try to write everything with computer vison and keras (if it works)

//we build face detection constructor
void face::object_detection(const cv::Mat& frame) {
    // we try something else
    std::ifstream ifs(std::string(face::classes).c_str()); //load the classes list
    std::string line;
    // Load in all the classes from the file
    while (getline(ifs, line))
    {
        std::cout << line << std::endl;
        class_names.emplace_back(line);
    }
    // Read in the neural network from the files
    cv::dnn::Net net = cv::dnn::readNet(weights, config, "TensorFlow"); // major bug
    // create blob from image
    cv::Mat blob = cv::dnn::blobFromImage(frame, 1.0, cv::Size(300, 300), cv::Scalar(127.5, 127.5, 127.5),true, false);
    net.setInput(blob);
    cv::Mat output = net.forward();
    // matrix with the result
    cv::Mat results(output.size[2], output.size[3], CV_32F, output.ptr<float>());
    // run through the result
    // Run through all the predictions
    for (int i = 0; i < results.rows; i++) {
        int class_id = int(results.at<float>(i, 1));
        float confidence = results.at<float>(i, 2);

        // Check if the detection is over the min threshold and then draw bbox
        if (confidence > min_confidence_score) {
            int bboxX = int(results.at<float>(i, 3) * frame.cols);
            int bboxY = int(results.at<float>(i, 4) * frame.rows);
            int bboxWidth = int(results.at<float>(i, 5) * frame.cols - bboxX);
            int bboxHeight = int(results.at<float>(i, 6) * frame.rows - bboxY);
            cv::rectangle(frame, cv::Point(bboxX, bboxY), cv::Point(bboxX + bboxWidth, bboxY + bboxHeight), cv::Scalar(0, 0, 255), 2);
            std::string class_name = class_names[class_id - 1];
            cv::putText(frame, class_name + " " + std::to_string(int(confidence * 100)) + "%", cv::Point(bboxX, bboxY - 10), cv::FONT_HERSHEY_SIMPLEX, 1.5, cv::Scalar(0, 255, 0), 2);
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
    const std::string path = "E:\\surge\\resources\\video1.mp4";
    cv::VideoCapture cap(path);
    cv::Mat frame;
    while (true) {
        cap.read(frame);
        resize(frame, frame, cv::Size(), 0.5, 0.5);
        auto start = cv::getTickCount();
        face.object_detection(frame); // function call for face detection
        auto end = cv::getTickCount();
        auto totalTime = (end - start) / cv::getTickFrequency();
        std::cout << "FPS :" << (1 / totalTime) << std::endl;
        cv::imshow("video", frame);
        cv::waitKey(1);
    };
}
