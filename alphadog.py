#!/usr/bin/env python
import os, shutil
import os.path
import sys
import argparse

parser = argparse.ArgumentParser(description='Split up files into folders based on various things about the filename')
parser.add_argument('directory', help='the directory you want to sort')
parser.add_argument('--sort', choices=["ALPHA", "EXTENSION"], help='sorts the files into subdirectories by alphabetical or extension')
parser.add_argument('--expand', action='store_true', help='expands subdirectories into a flat directory structure')
parser.add_argument('--target', help='directory to expand or sort into')
parser.add_argument('--move', action='store_true', help='if this option is selected, the files are moved rather than copied')
parser.add_argument('--max_files', default=-1, type=int, help='max files per directory')

# Pull values off of command line
args = parser.parse_args()
directory = args.directory
target = args.target
sort = args.sort
expand = args.expand
move = args.move
max_files = args.max_files

directory_files = {}

if target == None:
	target = directory

while directory[-1] == "\\" or directory[-1] == "/":
	directory = directory[0:-1]

while target[-1] == "\\" or target[-1] == "/":
	target = target[0:-1]

if not os.path.exists(directory):
	print "DIRECTORY " + directory + " DOESN'T EXIST"
	sys.exit()

if not os.path.exists(target):
	print "CREATING " + target
	os.makedirs(target)

print "PROCESSING: " + directory

# Sorting files
if sort:
	print "SORTING"
	for root, subdirs, files in os.walk(directory):
		for file in files:
			if sort == "ALPHA":
				name = file.capitalize()[0]
			elif sort == "EXTENSION":
				name = "_"
				parts = file.split(".")
				if len(parts) > 1:
					name = parts[-1]

			src = root + "/" + file
			dst = target + "/" + name

			print "PROCESSING " + src

			if not directory_files.has_key(name):
				directory_files[name] = 0

			directory_files[name] = directory_files[name] + 1

			if max_files > 0 and directory_files[name] > max_files:
				n = int(directory_files[name]/max_files)
				dst = dst + "(" + str(n) + ")"

			if not os.path.exists(dst):
				print "CREATING " + dst
				os.makedirs(dst)

			if move:
				print "MOVING " + src + " TO " + dst
				shutil.move(src, dst)
			else:
				print "COPYING " + src + " TO " + dst
				shutil.copy2(src, dst)
		break
elif expand:
	print "EXPANDING"
	for root, subdirs, files in os.walk(directory):
		for file in files:
			src = root + "/" + file
			dst = target + "/" + file

			print "PROCESSING " + src

			if move:
				print "MOVING " + src + " TO " + dst
				shutil.move(src, dst)
			else:
				print "COPYING " + src + " TO " + dst
				shutil.copy2(src, dst)