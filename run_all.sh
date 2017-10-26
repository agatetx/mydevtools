#!/bin/bash
sudo python update_img_local.py
./install-opencv.sh
./install_caffe.sh
./install_deep.sh
sudo python single_time_setups.py
