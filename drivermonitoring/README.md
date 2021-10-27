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
we link up to car ECU via obd2 port to monitor aggressive driving styles

1.Sudden Accelerations or Decelerations
2.Sudden Braking
3.Sharp Turns
4.Set of events like start, stop, speed and turns
5.Maximum and minimum rpm of the engine
6.Number of Red light Jumps
7.Number of Tailgating cases
8.Number of Aggressive Honking
9.Number of Wrong side Overtaking

### Built With

The code has been primarily written in python but will soon be ported to c++ for speed and efficiency, here are some of the languages used (or planning to be used) in the final distribution

* [python](https://www.python.org/)
* [Java](https://www.java.com/)
* [bash](https://www.gnu.org/software/bash/)
* [javascript](https://www.javascript.com/)

## Getting Started

All you need is git and python installed in your machine

for linux users:
* git
  ```sh
  sudo apt-get install git

* git
  ```sh
  sudo apt-get install python3
  
for windows users:
1. install [git](https://git-scm.com/downloads) using the link.
2. install [python3](https://www.python.org/downloads/)
### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/syno3/surge.git
   ```
2. Install the requirements
   ```sh
   pip install -r requirements.txt
   ```
3. Cd into the installed directory
   ```sh
   cd surge/drivermonitoring
   ```
4. run the python file
   ```sh
   python main.py
   ```

## Usage

if you want to get started in using DSM please read the following doc, it will give a great guide into how we implemented the full system from scratch. Incase of any inconsisntencies or grammatical errors please feel free to post the issue

_please refer to the [Documentation](documentation.md)_

<!-- ROADMAP -->
## Roadmap

- [] Move the codebase to java
- [X] Add user Interface
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
