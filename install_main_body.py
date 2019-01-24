
import os

os.system("apt-get -y update")
os.system("apt-get -y upgrade")

user = 'USERNAME'
#careate bush script for install libs
apt_packs=[
    'python-pip',
    'python3-pip',
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
    "iotop",
    "gparted",
    ]
for p in apt_packs:
    os.system("apt-get install -y "+p)


# Python3 tools
os.system("add-apt-repository -y ppa:mystic-mirage/pycharm")
os.system("apt-get update")
os.system("apt-get install -y pycharm-community")

os.system("pip3 install numpy scipy zmq spyder cython ipdb rpdb jupyter scikit-image cffi sklearn h5py tqdm more_itertools")
os.system("pip install numpy scipy zmq ipdb rpdb scikit-image cffi sklearn h5py tqdm more_itertools")


#Jupyter Lab
os.system("pip install jupyterlab")
os.system("jupyter serverextension enable --py jupyterlab --sys-prefix")


# wxPython
os.system('apt-get install -y libgtk2.0-dev libgtk-3-dev libjpeg-dev libtiff-dev libsdl1.2-dev libgstreamer-plugins-base0.10-dev libnotify-dev freeglut3 freeglut3-dev libsm-dev libwebkitgtk-dev libwebkitgtk-3.0-dev')
os.system("sudo pip install --upgrade --pre -f https://wxpython.org/Phoenix/snapshot-builds/ wxPython")


# Cafiene to Prevent Screen-Saver
os.system("add-apt-repository -y ppa:caffeine-developers/ppa")
os.system("apt-get update")
os.system("apt-get install -y caffeine")


# Nomachine
os.system('wget http://download.nomachine.com/download/6.0/Linux/nomachine_6.0.66_2_amd64.deb')
os.system('dpkg -i nomachine_6.0.66_2_amd64.deb')



os.system('echo ..............................................................................')
os.system('echo All packages have been installed sucessfully, hopefully.')
os.system('echo Cheers!')
os.system('echo ..............................................................................')

# MANUAL
# NOMACHINE
