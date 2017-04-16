#####
# This provides the qemu-arm-static binary
#apt-get install qemu-user-static

# Mount my target filesystem on /mnt
#mount -o loop fs.img /mnt

# Copy the static ARM binary that provides emulation
#cp $(which qemu-arm-static) /mnt/usr/bin
# Or, more simply: cp /usr/bin/qemu-arm-static /mnt/usr/bin

# Finally chroot into /mnt, then run 'qemu-arm-static bash'
# This chroots; runs the emulator; and the emulator runs bash
#chroot /mnt qemu-arm-static /bin/bash

###unmounting
#sudo umount /dev/mapper/loop0p1
#sudo umount /dev/mapper/loop0p2
#kpartx -d xu4_15.04_Master_21092015_m0.img
###

import argparse,os
#import pdb; pdb.set_trace()


#careate bush script for install libs
apt_packs=[
    'python-numpy',
    'python-scipy',
    'python-opencv',
    'python-pip',
    'python-zmq',
    'ffmpeg',
    "libx264-dev",
    "libx265-dev",
    "ipython",
    "screen",
    "tortoisehg",
    "git-gui",
    "bash-completion",
    "python-optcomplete",
    "vim",
    "cmake-gui",
    "libgeos-dev",
    "v4l-utils",
    "spyder",
    "pacman",
    "sshfs",
    "tortoisehg",
    "python-serial",
    "subversion",
    "axel",
    "wget",
    "zip",
    "unzip",
    "cmake",
    "build-essential",
    "dcraw",
    "lsof",
    "ros-indigo-desktop-full",
    "python-rosinstall",
    "kdiff3",
    "gitg",
    "strace",
    "wireshark",
    "gawk",
    "python-ipdb",
    "cython",
    "ipython-notebook",
    "ros-indigo-camera-info-manager-py",
    "k3b",
    "gstreamer1.0-libav",
    "gstreamer1.0-plugins-base-apps", 
    "gstreamer1.0-plugins-good",
    "gstreamer1.0-plugins-ugly",
    "exfat-utils",
    "python-osmgpsmap",
    "tshark",
    "wireshark-dev",
    "nmap",
    "chromium-browser",
    "arduino",
    "samba",
    "imagemagick",
    "python-gtk2-dev",
    "libosmgpsmap-dev",
    "libsoup2.4-dev",
"libgtk-3-dev",
"gobject-introspection",
"libpopt-dev",
"tmux"

    ]

# Python3 tools
os.system("add-apt-repository -y ppa:mystic-mirage/pycharm")
os.system("apt-get update")
os.system("apt-get install -y pycharm-community")

for p in apt_packs:
    os.system("apt-get install -y "+p)

pip_pkgs=[
    'shapely',
    'rpdb',
    'pudb',
    'jupyter',
    'rawpy'
    ]
for p in pip_pkgs:
    os.system('pip install ' + p) 



os.system("mkdir /disk2")
os.system("chmod taboon.taboon /disk2")


# Install  mavproxy 1.3.13
if not os.path.isdir('/MAVProxy-1.3.13'):
    os.system("wget https://pypi.python.org/packages/source/M/MAVProxy/MAVProxy-1.3.13.tar.gz#md5=1477eb38942c1718ee8311cf947fec50")
    os.system("tar xvzf MAVProxy-1.3.13.tar.gz")
    os.system("cd MAVProxy-1.3.13")
    os.system("python setup.py install")
    os.system("cd /")



# Download Thirdparty
os.system("wget https://www.dropbox.com/s/k3olqvz9ghsln1m/third_party_012016.tar.gz?dl=0 -O third_party.tar.gz")
os.system("tar xvf third_party.tar.gz")



# Install apmplanner2
os.system("cd third_party/")
os.system("dpkg -i apm_planner2_latest_ubuntu_trusty64.deb")
os.system("cd ~")




# Install POLYGON
os.system("cd third_party/Polygon-1.17/")
os.system(" python setup.py install")
os.system("cd ~")




# Install MVBLUEFOX
os.system("cd ~/third_party/mvBluefox/install_x86")
os.system("chmod +x install_mvGenTL_Acquire.sh")
os.system(r"""printf "y\ny\ny\ny\ny\n" | ./install_mvGenTL_Acquire.sh""")
os.system("cd ~")



# Install HELLCREST IMU
os.system("cp ~/third_party/Hillcrest/runtime/44-hillcrest.rules /etc/udev/rules.d/")



# Get ardupilot
os.system("git clone https://github.com/diydrones/ardupilot.git")



# Build GNURADIO
os.system("useradd -G dialout odorid")
os.system("groupadd usrp")
os.system(r"""echo 'ACTION=="add", BUS=="usb", SYSFS{idVendor}=="fffe", SYSFS{idProduct}=="0002", GROUP:="usrp", MODE:="0660"' > tmpfile""")
os.system("chown root.root tmpfile")
os.system("mv tmpfile /etc/udev/rules.d/10-usrp.rules")
os.system("cd ~")
os.system(r"""axel http://www.sbrac.org/files/build-gnuradio && chmod a+x ./build-gnuradio && printf "y\ny\ny\ny\ny\n" | ./build-gnuradio -ja""")




# INSTALL GAZEIBO from http://dev.ardupilot.com/wiki/using-rosgazebo-simulator-with-sitl/

git clone https://github.com/alexbuyval/ardupilot
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
catkin_init_workspace
cd ~/catkin_ws/
catkin_make
source devel/setup.bash
echo $ROS_PACKAGE_PATH
sudo apt-get install ros-indigo-octomap-msgs
roscd
cd ../src 
git clone https://alexbuyval@bitbucket.org/alexbuyval/arducopter_sitl_ros.git
git clone https://github.com/PX4/mav_comm.git
git clone https://github.com/alexbuyval/rotors_simulator.git 
git clone https://github.com/ethz-asl/glog_catkin.git
git clone https://github.com/catkin/catkin_simple.git
git clone https://github.com/ethz-asl/gflags_catkin.git
cd rotors_simulator
git checkout sonar_plugin
cd ../..
wstool init src 
wstool set -t src mavros --git https://github.com/alexbuyval/mavros.git
wstool update -t src 
rosdep install --from-paths src --ignore-src --rosdistro indigo -y
catkin_make
printf 'export PATH=$PATH:$HOME/ardupilot/Tools/autotest\n' >> ~/.bashrc
cd ~/ardupilot/ArduCopter
sudo apt-get purge modemmanager
cd ~/catkin_ws/
source devel/setup.bash
sim_vehicle.sh -f arducopter_sitl_ros --console

gnome-terminal --tab -t "razeebo sim" -e 'bash -c "cd ~/catkin_ws/ && source devel/setup.bash && cd ~/ardupilot/ArduCopter/ && sim_vehicle.sh -f arducopter_sitl_ros --console && sleep 20s"' 

# INSTALL SVO from http://rpg.ifi.uzh.ch/software_datasets.html
mkdir ~/workspace
cd ~/workspace
git clone https://github.com/strasdat/Sophus.git
cd Sophus
git checkout a621ff
mkdir build
cd build
cmake ..
makegnome-terminal --tab-with-profile="Default" -e 'sh -c '\''export TAB=1; exec bash'\' \
               --tab-with-profile="Default" -e 'sh -c '\''export TAB=2; exec bash'\' \
               --window-with-profile="Default" -e 'htop' \
               --tab-with-profile="Default" -e 'iotop'

cd ~/workspace
git clone https://github.com/uzh-rpg/fast.git
cd fast
mkdir build
cd build
cmake ..
make

cd ~/catkin_ws/src
git clone https://github.com/uzh-rpg/rpg_vikit.git
sudo apt-get install ros-indigo-cmake-modules

cd catkin_ws/src
git clone https://github.com/uzh-rpg/rpg_svo.git

FIX: ADD to ~/catkin_ws/src/rpg_vikit/vikit_common/CMakeLists.txt:
# Create vikit library
SET(Sophus_LIBRARIES libSophus.so)

catkin_make


RUN WITH:

gnome-terminal --tab -t "roscore" -e 'bash -c "cd ~/catkin_ws/ && source devel/setup.bash && roscore && sleep 20s"' --tab -t "rosrun rviz" -e 'bash -c "cd ~/catkin_ws/ && source devel/setup.bash && rosrun rviz rviz -d ~/catkin_ws/src/rpg_svo/svo_ros/rviz_config.rviz && sleep 20s"' --tab -t "rosrun rqt_svo" -e 'bash -c "cd ~/catkin_ws/ && source devel/setup.bash && rosrun rqt_svo rqt_svo && sleep 20s"' --tab -t "roslaunch svo_ros" -e 'bash -c "sleep 3s && cd ~/catkin_ws/ && source devel/setup.bash && cd ~/catkin_ws/src/rpg_svo/svo_ros/launch/ && roslaunch svo_ros test_rig3.launch && sleep 20s"' --tab -t "play bag file" -e 'bash -c "rosbag play ~/DATA/airground_rig_s3_2013-03-18_21-38-48.bag"' 

roscore

cd ~/catkin_ws/
source devel/setup.bash
rm ~/.config/ros.org/rqt_gui.ini
rosrun rqt_svo rqt_svo

cd ~/catkin_ws/
source devel/setup.bash
rosrun rviz rviz -d ~/catkin_ws/src/rpg_svo/svo_ros/rviz_config.rviz

cd ~/catkin_ws/
source devel/setup.bash
cd /home/taboon/catkin_ws/src/rpg_svo/svo_ros/launch/
cd ~/catkin_ws/src/rpg_svo/svo_ros/launch/
roslaunch svo_ros test_rig3.launch

rosbag play ~/Downloads/airground_rig_s3_2013-03-18_21-38-48.bag





# RUN LSD-SLAM http://vision.in.tum.de/research/vslam/lsdslam

gnome-terminal --tab -t "roscore" -e 'bash -c "roscore && sleep 20s"' --tab -t "lsd_slam_viewer" -e 'bash -c "rosrun lsd_slam_viewer viewer && sleep 20s"' --tab -t "rosrun rqt_svo" -e 'bash -c "rosrun lsd_slam_core live_slam image:=/image_raw camera_info:=/camera_info && sleep 20s"' --tab -t "play bag file" -e 'bash -c "rosbag play ~/DATA/LSD_room.bag"' 

gnome-terminal --tab -t "roscore" -e 'bash -c "roscore && sleep 20s"' --tab -t "lsd_slam_viewer" -e 'bash -c "rosrun lsd_slam_viewer viewer && sleep 20s"' --tab -t "rosrun rqt_svo" -e 'bash -c "rosrun lsd_slam_core live_slam image:=/image_raw camera_info:=/camera_info && sleep 20s"' --tab -t "play bag file" -e 'bash -c "rosbag play /media/taboon/6E2200D9254014D4/LSD_foodcourt.bag"' 


# INSTALL gr-ieee802-11 from https://github.com/bastibl/gr-ieee802-11
sudo apt-get install libitpp-dev
sudo apt-get install liblog4cpp5-dev

cd ~
git clone https://github.com/bastibl/gr-foo.git
cd gr-foo
mkdir build
cd build
cmake ..
make
sudo make install
sudo ldconfig

cd ~
git clone git://github.com/bastibl/gr-ieee802-11.git
cd gr-ieee802-11
mkdir build
cd build
cmake ..
make
sudo make install
sudo ldconfig


# Run with:
mkfifo /tmp/ofdm.bin
wireshark
gnuradio-companion ~/gr-foo/build/gr-ieee802-11/examples/wifi_phy_hier.grc




# INSTALL CAFFE according to: http://hanzratech.in/2015/07/27/installing-caffe-on-ubuntu.html

cd ~
mkdir deep-learning
cd deep-learning
sudo apt-get install libprotobuf-dev libleveldb-dev libsnappy-dev libopencv-dev libhdf5-serial-dev protobuf-compiler
sudo apt-get install --no-install-recommends libboost-all-dev 
sudo apt-get install libatlas-base-dev
sudo apt-get install the python-dev
sudo apt-get install libgflags-dev libgoogle-glog-dev liblmdb-dev
make all 
make test 
make runtest

cd ~/deep-learning/caffe 
make pycaffe 
echo export PYTHONPATH=$PYTHONPATH:$HOME/deep-learning/caffe/python >> ~/.bashrc 


cd ~/deep-learning 
wget http://dl.caffe.berkeleyvision.org/bvlc_googlenet.caffemodel 
mv bvlc_googlenet.caffemodel caffe/models/bvlc_googlenet/ 
git clone https://github.com/google/deepdream.git 
sudo pip install protobuf 
sudo pip install scikit-image
sudo pip install tornado --upgrade

# RUN USING:
cd ~/deep-learning/deepdream 
ipython notebook
sudo apt-get install python-pandas





# SITL from http://dev.ardupilot.com/wiki/setting-up-sitl-on-linux/
cd ~/ardupilot/ArduPlane
../Tools/autotest/sim_vehicle.sh -w
../Tools/autotest/sim_vehicle.sh --console --map --aircraft test
wp load ../Tools/autotest/ArduPlane-Missions/CMAC-toff-loop.txt
arm throttle
mode auto



# JSBSIM
cd ~/ardupilot/Tools/autotest/aircraft/Rascal


# osm-gps-map
map: http://maptile.maps.svc.ovi.com/maptiler/maptile/newest/satellite.day/#Z/#X/#Y/256/png8


# thermapp install and rub:





##to work in gnuradio:
#add to ~/.bashrc
#LANG= 
#LC_ADDRESS= 
#LC_IDENTIFICATION= 
#LC_MEASUREMENT= 
#LC_MONETARY= 
#LC_NAME= 
#LC_NUMERIC= 
#LC_PAPER= 
#LC_TELEPHONE= 
#LC_TIME=


#os.system("chmod +x install.sh")
#os.system("usermod -a -G usrp odroid")


