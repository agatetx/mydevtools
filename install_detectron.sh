sudo apt-get update
sudo apt-get install -y --no-install-recommends \
      build-essential \
      cmake \
      git \
      libgoogle-glog-dev \
      libgtest-dev \
      libiomp-dev \
      libleveldb-dev \
      liblmdb-dev \
      libopencv-dev \
      libopenmpi-dev \
      libsnappy-dev \
      libprotobuf-dev \
      openmpi-bin \
      openmpi-doc \
      protobuf-compiler \
                       
sudo pip3 future protobuf

sudo apt-get install -y --no-install-recommends libgflags-dev

git clone https://github.com/pytorch/pytorch.git && cd pytorch
git submodule update --init --recursive
sudo python3 setup.py install




COCOAPI=~/cocoapi
git clone https://github.com/cocodataset/cocoapi.git $COCOAPI
cd $COCOAPI/PythonAPI
sudo python3 setup.py install

cd ~
DETECTRON=~/detectron
git clone https://github.com/facebookresearch/detectron $DETECTRON
sudo pip3 install -r $DETECTRON/requirements.txt
cd $DETECTRON && make


sudo apt-get install graphviz
sudo pip3 install hypothesis
cd ~ && python3 -c 'from caffe2.python import core' 2>/dev/null && echo "CAFFE2: Success" || echo "CAFFE2: Failure"
