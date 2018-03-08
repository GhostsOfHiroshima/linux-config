#!/usr/bin/python2.7
# Wallpaper changer

import os
import os.path
from random import choice
from time import sleep

# pictures root folder
PICTURES_FOLDER = '/home/icebox/Pictures/wallpapers'
ROTATE_EVERY = 60	# minutes
# valid extensions
EXTENSIONS = [
	'PNG',
	'JPG',
	'BMP',
	'JPEG'
]

# checks if file has a good extension
def good_extension(f):
	f = f.lower()
	for e in EXTENSIONS:
		if f.endswith(e.lower()):
			return True
	return False

# list all files in dir and subdir
def files_in_dir(d):
	l = []
	for dirpath, dirnames, filenames in os.walk(d):
		for filename in [f for f in filenames if good_extension(f)]:
			f = os.path.join(dirpath, filename)
			l.append(f)
	return l
	
def set_random_wallpaper():
	files = files_in_dir(PICTURES_FOLDER)
	if not files: 
		print '[!] no pictures in folder/s' 
		return	# if no files, return
	f = choice(files)		# get random file
	cmd = 'feh --bg-fill {}'.format(f)
	os.system(cmd)		# set wallpaper

# main method
def main():
	while True:
		set_random_wallpaper()
		sleep(60 * ROTATE_EVERY)
	
main()	
