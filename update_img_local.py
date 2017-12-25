
import os

os.system("apt-get -y update")
os.system("apt-get -y upgrade")

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

# Cuda
os.system('wget https://developer.nvidia.com/compute/cuda/8.0/Prod2/local_installers/cuda-repo-ubuntu1604-8-0-local-ga2_8.0.61-1_amd64-deb -O cuda.deb')
os.system("dpkg -i cuda.deb")
os.system("apt-get -y update")
os.system("apt-get -y install cuda")
os.system("pip3 install tensorflow-gpu")
os.system("pip install tensorflow-gpu")


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
os.system('timedatectl set-timezone Asia/Jerusalem')
os.system('updatedb &> /dev/null')


# Handle nvidia version HELL
os.system('apt -y remove nvidia-3*')
os.system('apt -y install nvidia-375-dev')


# Nomachine
os.system('wget http://download.nomachine.com/download/6.0/Linux/nomachine_6.0.66_2_amd64.deb')
os.system('dpkg -i nomachine_6.0.66_2_amd64.deb')



os.system('echo ..............................................................................')
os.system('echo All packages have been installed sucessfully (hopefully).')
os.system('echo Cheers!')
os.system('echo ..............................................................................')

# MANUAL
# NOMACHINE
