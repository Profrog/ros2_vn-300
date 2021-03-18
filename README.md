# ros2_vn-300


i use linux ubuntu 20.04
using note book : hp-pavilion-gaming-laptop-16-a000x
ros2 version : foxy : 

other movie and picture link : https://blog.naver.com/ache159/222279288818


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


