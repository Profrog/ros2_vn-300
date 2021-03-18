import os
import subprocess


os.system("cd ~/ros2_vn-300/dev_ws/src")
os.system("rosdep install -i --from-path src --rosdistro foxy -y")
os.system("colcon build --packages-select py_pubsub")

subprocess.call('/bin/bash -c "$GREPDB"' , shell = True, env = {'GREPDB' : 'source /opt/ros/foxy/setup.bash'})
subprocess.call('/bin/bash -c "$GREPDB"' , shell = True, env = {'GREPDB' : '. install/setup.bash'})

