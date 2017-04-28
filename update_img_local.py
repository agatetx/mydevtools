
import os

user = 'USERNAME'
#careate bush script for install libs
apt_packs=[
    'ffmpeg',
    "screen",
    "git-gui",
    "bash-completion",
    "sshfs",
    "cmake",
    "build-essential",
    "kdiff3",
    "nmap",
    "chromium-browser",
    "arduino",
    "samba",
    "imagemagick",
    "tmux",
    "unzip",
    "wget",
    "nano",
    "terminator",
    "vlc",
    "htop"
    ]
for p in apt_packs:
    os.system("apt-get install -y "+p)


# Python3 tools
os.system("add-apt-repository -y ppa:mystic-mirage/pycharm")
os.system("apt-get update")
os.system("apt-get install -y pycharm-community")
os.system("apt-get install -y python-pip python3-pip")
os.system("pip3 install numpy scipy zmq spyder cython ipdb rpdb pyqt5 jupyter tensorflow")
os.system("pip install numpy scipy zmq ipdb rpdb pyqt5 tensorflow")


# Cafiene to Prevent Screen-Saver
os.system("add-apt-repository -y ppa:caffeine-developers/ppa")
os.system("apt-get update")
os.system("apt-get install -y caffeine")

# cd ~ ; ./src/mydevtools/install-opencv.sh | tee output_opencv.txt

# MANUAL
# NOMACHINE
