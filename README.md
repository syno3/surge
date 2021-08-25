## What is surge? 

Is a level 2 self driving system that performs functions like Adaptive cruise control (ACC), Automated Lane Centering (ALC), Fowards Collision Warning (FCW) and Lane Departure Wanring (LDW) and uses data from it vision system to determine the appropriate driving path, speed, throtle and velocity.

### How does it work

We system is built in python and will be deployed in c++ to increase speed and efficiency. We use normal computer vision to get data from a camera module installed as a dashcam. The data from the camera goes through various processes (ie.) Lane detection, object detection, semantic segmentation, Visual Odometry and motion planning to output a driving signals. The signals are then sent to the car ECU via an OBD2 port connection in the car.

### Limitation of surge

Using basic computer vision comes with its fair of downsides (ie.):
<ul>
    <li> The system lacks a dynamic approach to outputing a driving tragectory
    <li> Poor visibility (heavy rain, snow, fog, etc.) or weather conditions that may interfere with sensor operation.
    <li> The road facing camera is obstructed, covered or damaged by mud, ice, snow, etc.
    <li> When in sharp curves, like on-off ramps, intersections etc...; openpilot is designed to be limited in the amount of steering torque it can produce.
    <li> When driving on highly banked roads or in presence of strong cross-wind.
    <li> Bright light (due to oncoming headlights, direct sunlight, etc.).
    <li> Driving on hills, narrow, or winding roads.
</ul>

### future upgrades

our goal is to use supervised LSTM in Reinforcement Learning combine both of its advantages (context and dynamic) nature to create a full end-to-end driving module that is dynamic and applies context from it pervious experience to output driving signals

### Developers

Me !!!!!




