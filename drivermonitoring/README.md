<div id="top"></div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="assets/whats-going-on-driving.gif" alt="Logo" width="640" height="480">
  </a>

  <h3 align="center">SURGE Driver-state-monitoring</h3>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## About The Project

The driver state monitoring, also known as driver attention monitor, is a vehicle safety system to assess the driver's alertness and warn the driver if needed and eventually apply the brakes. It was first introduced by Toyota in 2006 for its and Lexus latest models. It was first offered in Japan on the GS 450h. The system's functions co-operate with the pre-collision system (PCS). The system uses infrared sensors to monitor driver attentiveness. Specifically, the driver monitoring system includes a CCD camera placed on the steering column which tracks the face, via infrared LED detectors. If the driver is not paying attention to the road ahead and a dangerous situation is detected, the system will warn the driver by flashing lights, warning sounds. If no action is taken, the vehicle will apply the brakes (a warning alarm will sound followed by a brief automatic application of the braking system).

## Aggressive Driving Style Criteria: (Input Variables)
we monitor for specific aggressive driving style behaviours like:

1. Sudden Accelerations or Decelerations
2. Sudden Braking
3. Sharp Turns
4. Set of events like start, stop, speed and turns
5. Maximum and minimum rpm of the engine
6. Number of Red light Jumps
7. Number of Tailgating cases
8. Number of Aggressive Honking
9. Number of Wrong side Overtaking

### Built With

The code has been primarily written in python but will soon be ported to c++ for speed and efficiency, here are some of the languages used (or planning to be used) in the final distribution

* [python](https://www.python.org/)
* [c++](https://isocpp.org/)
* [bash](https://www.gnu.org/software/bash/)
* [javascript](https://www.javascript.com/)

## Getting Started and Installation

Please follow closely the following installation instruction for linux and windows users

for linux users:
you need to start-off by installing opencv on your machine:
* bash
  ```sh
  sudo apt -y remove x264 libx264-dev

after that install g++ compiler and other dependancies
* bash
  ```sh
  sudo apt -y install build-essential checkinstall cmake pkg-config yasm
  sudo apt -y install git gfortran
  sudo apt -y install libjpeg8-dev libjasper-dev libpng12-dev
  sudo apt -y install libtiff5-dev
  sudo apt -y install libtiff-dev
  sudo apt -y install libavcodec-dev libavformat-dev libswscale-dev libdc1394-22-dev
  sudo apt -y install libxine2-dev libv4l-dev
  cd /usr/include/linux
  sudo ln -s -f ../libv4l1-videodev.h videodev.h
  cd $cwd


* bash
  ```sh
  sudo apt -y install libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev
  sudo apt -y install libgtk2.0-dev libtbb-dev qt5-default
  sudo apt -y install libatlas-base-dev
  sudo apt -y install libfaac-dev libmp3lame-dev libtheora-dev
  sudo apt -y install libvorbis-dev libxvidcore-dev
  sudo apt -y install libopencore-amrnb-dev libopencore-amrwb-dev
  sudo apt -y install libavresample-dev
  sudo apt -y install x264 v4l-utils

other optional dependancies

* bash
  ```sh
  sudo apt -y install libprotobuf-dev protobuf-compiler
  sudo apt -y install libgoogle-glog-dev libgflags-dev
  sudo apt -y install libgphoto2-dev libeigen3-dev libhdf5-dev doxygen

install python and some libraries
* bash
  ```sh
  sudo apt -y install python3-dev python3-pip
  sudo -H pip3 install -U pip numpy
  sudo apt -y install python3-testresources

install virtualenv and virtualenvwrapper modules to create Python virtual environments.
* bash
  ```sh
  cd $cwd
  python3 -m venv OpenCV-"$cvVersion"-py3
  echo "# Virtual Environment Wrapper" >> ~/.bashrc
  echo "alias workoncv-$cvVersion=\"source $cwd/OpenCV-$cvVersion-py3/bin/activate\"" >> ~/.bashrc
  source "$cwd"/OpenCV-"$cvVersion"-py3/bin/activate

now install python libraries within this virtual environment
* bash
  ```sh
  pip install wheel numpy scipy matplotlib scikit-image scikit-learn ipython dlib

quit virtual environment
* bash
  ```sh
  deactivate

download opencv and opencv_contrib
* bash
  ```sh
  git clone https://github.com/opencv/opencv.git
  cd opencv
  git checkout $cvVersion
  cd ..
  git clone https://github.com/opencv/opencv_contrib.git
  cd opencv_contrib
  git checkout $cvVersion
  cd ..

compile opencv with opencv_contrib
* bash
  ```sh
  cd opencv
  mkdir build
  cd build

we start compilation process
* bash
  ```sh
  cmake -D CMAKE_BUILD_TYPE=RELEASE \
            -D CMAKE_INSTALL_PREFIX=$cwd/installation/OpenCV-"$cvVersion" \
            -D INSTALL_C_EXAMPLES=ON \
            -D INSTALL_PYTHON_EXAMPLES=ON \
            -D WITH_TBB=ON \
            -D WITH_V4L=ON \
            -D OPENCV_PYTHON3_INSTALL_PATH=$cwd/OpenCV-$cvVersion-py3/lib/python3.5/site-packages \
        -D WITH_QT=ON \
        -D WITH_OPENGL=ON \
        -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules \
        -D BUILD_EXAMPLES=ON ..

we build the package
* bash
  ```sh
    make -j4
    make install

create CMakeLists.txt file and add
* bash
  ```sh
    cmake_minimum_required(VERSION 3.1)
    # Enable C++11
    set(CMAKE_CXX_STANDARD 11)
    set(CMAKE_CXX_STANDARD_REQUIRED TRUE)
    
set opencv dir and opencv_home dir
* bash
  ```sh
    SET(OpenCV_DIR <OpenCV_Home_Dir>/installation/OpenCV-master/lib/cmake/opencv4)
    SET(OpenCV_DIR /home/hp/OpenCV_installation/installation/OpenCV-master/lib/cmake/opencv4)

run the actual program
* bash
  ```sh
    mkdir build && cd build
    cmake ..
    cmake --build . --config Release
    
for windows users:
1. install [git](https://git-scm.com/downloads) using the link.
2. install [python3](https://www.python.org/downloads/)
3. install opencv C++ [opencv 4.1.2 c++](https://subwaymatch.medium.com/opencv-410-with-vs-2019-3d0bc0c81d96)

## Usage

if you want to get started in using DSM please read the following doc, it will give a great guide into how we implemented the full system from scratch. Incase of any inconsisntencies or grammatical errors please feel free to post the issue

_please refer to the [Documentation](documentation.md)_

<!-- ROADMAP -->
## Roadmap

- [X] Move the codebase to c++
- [X] Add user Interface
- [] Fix bugs
- [] Upadte readme
- [] Create custom dataset
- [] create graphics
- [] Make the interface dynaminc
- [] Create visuals for the product
- [] Add the prediction algorithim
- [X] Add face pose and orientation coordinates
- [X] Move to mediapipe
- [] speed up the code
- [X] Add image adjustments
- [X] Add distance measurement to reduce false (+ve's)
- [] fix issues with sunglasses
- [X] clean redundant code
- [] Intergrate with CAN buses in cars
- [X] Add more parameters to track
- [] Multi-language Support
    - [] Chinese
    - [] Spanish

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

## Contact

Your Name - [@festus_mk](https://twitter.com/your_username) - sinotechxvista@gmail.com

Project Link: [syno3](https://github.com/syno3/surge)
