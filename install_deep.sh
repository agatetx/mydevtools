import os
import argparse

parser = argparse.ArgumentParser(description='Install DL frameworks.')
parser.add_argument("--use_cuda", action='store_true')

args = parser.parse_args()

os.system('sudo pip install keras torchvision visdom')
os.system('sudo pip3 install keras torchvision visdom')

if args.use_cuda:
    os.system('sudo pip3 install http://download.pytorch.org/whl/cu80/torch-0.3.0.post4-cp35-cp35m-linux_x86_64.whl')
    os.system('sudo pip install http://download.pytorch.org/whl/cu80/torch-0.3.0.post4-cp27-cp27mu-linux_x86_64.whl') 
    os.system('sudo pip3 install tensorflow-gpu')
    os.system('sudo pip install tensorflow-gpu')
else:
    os.system('sudo pip3 install http://download.pytorch.org/whl/cpu/torch-0.3.0.post4-cp35-cp35m-linux_x86_64.whl ')
    os.system('sudo pip install http://download.pytorch.org/whl/cpu/torch-0.3.0.post4-cp27-cp27mu-linux_x86_64.whl ') 
    os.system('sudo pip3 install tensorflow')
    os.system('sudo pip install tensorflow')
 
#sudo pip install dlib
#sudo pip3 install dlib
#sudo pip install Theano 

