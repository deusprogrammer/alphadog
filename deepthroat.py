#!/usr/bin/env python
import os, shutil
import os.path
import sys
import argparse
import re

parser = argparse.ArgumentParser(description='Split up files into folders based on various things about the filename')
parser.add_argument('directory', help='the directory you want to copy from')
parser.add_argument('--target', help='directory to copy into')
parser.add_argument('--regex', help='regex pattern of filenames to copy')

# Pull values off of command line
args = parser.parse_args()
directory = args.directory
target = args.target
regex = args.regex

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

print "REGEX:      " + regex
p = re.compile(regex)

print "PROCESSING: " + directory

for root, subdirs, files in os.walk(directory):
	for file in files:
		if p.search(file) == None:
			continue

		src = root + "/" + file
		dst = target + "/" + file

		print "PROCESSING " + src

		print "COPYING " + src + " TO " + dst
		shutil.copy2(src, dst)