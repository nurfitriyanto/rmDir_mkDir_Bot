#!/usr/bin/python
import os
import sys
import shutil
import time

# Get dir name
_directory = '/home/plendock/Pictures/tes/'

# function to make directory
def make_dir(path, mode):
    if not path or os.path.exists(path):
        return []
    (head, tail) = os.path.split(path)
    res = supermakedirs(head, mode)
    os.mkdir(path)
    os.chmod(path, mode)
    res += [path]
    return res
    
while True:
    _time_now = time.strftime("%H:%M")
    print(_time_now)
    try:
        if _time_now == '02:27': #set time to execute
            print('crrooooot')
            shutil.rmtree(_directory)
            make_dir(path=_directory, mode=0777)
        else:
            print('waitttt')
    except Exception as e:
        print(e)
    time.sleep(60)
