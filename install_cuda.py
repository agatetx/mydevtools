import os

# Cuda
os.system('wget https://developer.nvidia.com/compute/cuda/8.0/Prod2/local_installers/cuda-repo-ubuntu1604-8-0-local-ga2_8.0.61-1_amd64-deb -O cuda.deb')
os.system("dpkg -i cuda.deb")
os.system("apt-get -y update")
os.system("apt-get -y install cuda")


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
