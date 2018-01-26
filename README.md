# mydevtools

These are my personal scripts to automatically install a linux 16.x machine with a complete machine-vision\deep-learning research environment. 

Usage instructions:
Option 1 - Install full machine:
- sudo apt-get install git, python
- git clone https://github.com/agatetx/mydevtools.git
- cd mydevtools
- sudo python install_machine.py --install_cuda --install_deep

Option 2 - Install packages separately:
- sudo apt-get install git, python
- git clone https://github.com/agatetx/mydevtools.git
- cd mydevtools
- sudo python install_main_body.py
- sudo python install_cuda.py
- ./install_opencv.sh
- sudo python install_deep.py --use_cuda
- python single_time_setups.py
