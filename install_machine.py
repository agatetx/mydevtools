import sys
import os
import argparse

parser = argparse.ArgumentParser(description='Install machine for ML and CV.')
parser.add_argument("--install_cuda", action='store_true')
parser.add_argument("--install_deep", action='store_true')

args = parser.parse_args()

os.system('sudo python install_main_body.py')


if args.install_cuda:
    os.system('sudo python install_cuda.py')

os.system('./install_opencv.sh')

if args.install_deep:
    os.system('sudo python install_deep.py ' + '--use_cuda' if args.install_cuda else '')




