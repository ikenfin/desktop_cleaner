#/usb/bin/python
# -*- coding: utf-8 -*-

import os, shutil, datetime

# simple script for cleaning desktop

# if true - prevent move symlinks
exclude_symlinks = True

# dir to clean
dir_name = '/home/ken/Desktop/'

# dir to store desktop items
out_dir_name = 'desktop_vn'

# exclude from cleaning
white_list = [
	'home',
	'just_job',
	'polytech',
	out_dir_name
]

from_dir = os.listdir(dir_name)

to_dir = dir_name + out_dir_name + '/' + datetime.date.today().strftime('%Y-%m-%d')

if os.path.exists(to_dir) == False :
	os.makedirs(to_dir)

for filename in from_dir :
    if(filename not in white_list) :
        if(not(exclude_symlinks) or not(os.path.islink(dir_name + filename))) :
            shutil.move(dir_name + filename, to_dir)
