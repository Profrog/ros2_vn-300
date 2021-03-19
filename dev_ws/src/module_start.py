import os
import subprocess
import sys
# from pipes import quote


sp = subprocess.Popen(['/bin/bash', '-c',"source /opt/ros/foxy/setup.bash"])
sp.communicate()

sp2 = subprocess.Popen(['/bin/bash', '-c',". install/setup.bash"])
sp2.communicate()

# os.system("cd ~/ros2_vn-300/dev_ws/src")
# os.system("rosdep install -i --from-path src --rosdistro foxy -y")
os.system("colcon build --packages-select py_pubsub")


# python, script = quote(sys.executable), quote(sys.argv[0])
# os.execl("/bin/bash", "/bin/bash", "-c", 'source /opt/ros/foxy/setup.bash;')
# os.execl("/bin/bash", "/bin/bash", "-c", '. install/setup.bash;')
# output = ("source /opt/ros/foxy/setup.bash; env -0",   shell=True , executable="/bin/bash")


# subprocess.run(["source", ""])
# subprocess.call('/bin/bash -c "$GREPDB"' , shell = True, env = {'GREPDB' : '. install/setup.bash'})

