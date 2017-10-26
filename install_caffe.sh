#!/bin/bash

sudo apt-get -y update

sudo apt-get -y upgrade

sudo apt-get install -y build-essential cmake git pkg-config

sudo apt-get install -y libprotobuf-dev libleveldb-dev libsnappy-dev libhdf5-serial-dev protobuf-compiler

sudo apt-get install -y libatlas-base-dev 

sudo apt-get install -y --no-install-recommends libboost-all-dev

sudo apt-get install -y libgflags-dev libgoogle-glog-dev liblmdb-dev

cd ~
rm -rf caffe
git clone https://github.com/BVLC/caffe
cd caffe

cp Makefile.config.example Makefile.config

sed -i s/"# OPENCV_VERSION := 3"/"OPENCV_VERSION := 3"/ Makefile.config
sed -i s/"# USE_CUDNN := 1"/"USE_CUDNN := 1"/ Makefile.config
sed -i s/"# WITH_PYTHON_LAYER := 1"/"WITH_PYTHON_LAYER := 1"/ Makefile.config
sed -i s/'INCLUDE_DIRS := $(PYTHON_INCLUDE) \/usr\/local\/include'/'INCLUDE_DIRS := $(PYTHON_INCLUDE) \/usr\/local\/include \/usr\/include\/hdf5\/serial \/opt\/cudnn\/cuda\/include\/'/ Makefile.config
sed -i s/'LIBRARY_DIRS := $(PYTHON_LIB) \/usr\/local\/lib \/usr\/lib'/'LIBRARY_DIRS := $(PYTHON_LIB) \/usr\/local\/lib \/usr\/lib \/usr\/lib\/x86_64-linux-gnu\/hdf5\/serial\/ \/opt\/cudnn\/cuda\/lib64 \/usr\/local\/cuda\/lib64\/'/ Makefile.config

make all -j10 && make test && make runtest && make pycaffe
