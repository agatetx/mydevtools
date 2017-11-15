
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
    "htop",
    "locate",
    ]
for p in apt_packs:
    os.system("apt-get install -y "+p)


# Python3 tools
os.system("add-apt-repository -y ppa:mystic-mirage/pycharm")
os.system("apt-get update")
os.system("apt-get install -y pycharm-community")
os.system("apt-get install -y python-pip python3-pip")
os.system("pip3 install numpy scipy zmq spyder cython ipdb rpdb pyqt5 jupyter scikit-image cffi sklearn h5py")
os.system("pip install numpy scipy zmq ipdb rpdb pyqt5 scikit-image cffi sklearn h5py")


# wPython
os.system('apt-get install -y libgtk2.0-dev libgtk-3-dev libjpeg-dev libtiff-dev libsdl1.2-dev libgstreamer-plugins-base0.10-dev libnotify-dev freeglut3 freeglut3-dev libsm-dev libwebkitgtk-dev libwebkitgtk-3.0-dev')
os.system("sudo pip install --upgrade --pre -f https://wxpython.org/Phoenix/snapshot-builds/ wxPython")


# Cafiene to Prevent Screen-Saver
os.system("add-apt-repository -y ppa:caffeine-developers/ppa")
os.system("apt-get update")
os.system("apt-get install -y caffeine")

# Cuda
os.system('wget https://developer.nvidia.com/compute/cuda/8.0/Prod2/local_installers/cuda-repo-ubuntu1604-8-0-local-ga2_8.0.61-1_amd64-deb -O cuda.deb')
os.system("dpkg -i cuda.deb")
os.system("sudo apt-get -y update")
os.system("sudo apt-get -y install cuda")
os.system("pip3 install -y tensorflow-gpu")
os.system("pip install -y tensorflow-gpu")

# Cudnn 6
os.system('wget https://www.dropbox.com/s/w2211kd0u0vgtgs/cudnn-8.0-linux-x64-v6.0.tgz?dl=0 -O cudnn.tgz')
os.system('rm -rf /opt/cudnn/')
os.system('mkdir /opt/cudnn/')
os.system('tar -xvzf cudnn.tgz -C /opt/cudnn/')

# Cudnn 5.1
os.system('wget https://www.dropbox.com/s/12hobmwc1ufxpqr/cudnn-8.0-linux-x64-v5.1.tgz?dl=0 -O cudnn-5.1.tgz')
os.system('rm -rf /opt/cudnn-5.1/')
os.system('mkdir /opt/cudnn-5.1/')
os.system('tar -xvzf cudnn-5.1.tgz -C /opt/cudnn-5.1/')


#os.system('mkdir /opt/cudnn/')
os.system('''echo 'export LD_LIBRARY_PATH=/opt/cudnn/cuda/lib64:$LD_LIBRARY_PATH' >>~/.bashrc''')
os.system('sudo timedatectl set-timezone Asia/Jerusalem')
os.system('sudo updatedb')



# cd ~ ; ./src/mydevtools/install-opencv.sh | tee output_opencv.txt

# MANUAL
# NOMACHINE
