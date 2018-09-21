import os

#Purge ALL nvidia
os.system('apt -y purge nvidia*')
os.system('apt -y purge cuda*')


# Cuda
os.system('wget https://developer.nvidia.com/compute/cuda/9.0/Prod/local_installers/cuda-repo-ubuntu1604-9-0-local_9.0.176-1_amd64-deb -O cuda.deb')
os.system('sudo apt-key add /var/cuda-repo-<version>/7fa2af80.pub')
os.system("dpkg -i cuda.deb")
os.system("apt-get -y update")
os.system("apt-get -y --allow-unauthenticated install cuda")
os.system("wget https://developer.nvidia.com/compute/cuda/9.0/Prod/patches/1/cuda-repo-ubuntu1604-9-0-local-cublas-performance-update_1.0-1_amd64-deb")
os.system("dpkg -i cuda-repo-ubuntu1604-9-0-local-cublas-performance-update_1.0-1_amd64-deb")

if 1:
    # Cudnn 7
    os.system('wget https://www.dropbox.com/s/a6jo871mclhb9e3/libcudnn7_7.0.5.15-1%2Bcuda9.1_amd64.deb -O cudnn-7.0.deb')
    os.system('sudo dpkg -i  cudnn-7.0.deb')
    os.system('wget https://www.dropbox.com/s/oyz8qnsgy7vhxhx/libcudnn7-dev_7.0.5.15-1%2Bcuda9.1_amd64.deb -O cudnn-dev-7.0.deb')
    os.system('sudo dpkg -i  cudnn-dev-7.0.deb')

if 0:
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



    os.system('''echo 'export LD_LIBRARY_PATH=/opt/cudnn/cuda/lib64:$LD_LIBRARY_PATH' >>~/.bashrc''')
    os.system('timedatectl set-timezone Asia/Jerusalem')
    os.system('updatedb &> /dev/null')


# Handle nvidia version HELL
os.system('apt -y remove nvidia-3*')
os.system('add-apt-repository -y ppa:graphics-drivers')
os.system('apt-get update')
os.system('apt -y --allow-unauthenticated install nvidia-390-dev')
