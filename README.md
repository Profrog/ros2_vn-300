# ros2_vn-300


i use linux ubuntu 20.04
using note book that 

![Screenshot from 2021-03-18 10-09-09](https://user-images.githubusercontent.com/26535065/111558391-08799600-87d2-11eb-8312-328f61734da1.png)

ros2 version : foxy

![20210303_154304_381](https://user-images.githubusercontent.com/26535065/111559314-9c982d00-87d3-11eb-9925-fa3f76e68c9c.jpg)

other movie and picture link : 


# topic list

* vn_time: print("Time_vn " + Time_vn)
* vn_yaw : print("Yaw_vn " + Yaw_vn) 
* vn_pitch : print("Pitch_vn " + Pitch_vn)
* vn_roll : print("Roll_vn " + Roll_vn)
* vn_latitude : print("Latitude_vn " + Latitude_vn)
* vn_altitude : print("Altitude_vn " + Altitude_vn)

of VNINS

Check about vn-300 and data in https://geo-matching.com/uploads/default/m/i/migrationawsfgl.pdf



# build 

* cd ~/ros2_vn-300/dev_ws
* rosdep install -i --from-path src --rosdistro foxy -y
* colcon build --packages-select py_pubsub
* . install/setup.bash


# run 
* source /opt/ros/foxy/setup.bash
* ros2 run py_pubsub vn_time


