#!/usr/bin/env python3
import os, sys

current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(current_dir + "/anthea")

os.chdir('anthea')
exec(open("./scrape.py").read())
exec(open("./parse.py").read())
os.chdir('..')
