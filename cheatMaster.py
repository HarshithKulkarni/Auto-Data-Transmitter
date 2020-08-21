import subprocess as sp
import os
import shutil
import sys

scrsht = str(sys.argv[1])
backup = str(sys.argv[2])


arr = []

while(1):
	ls = os.listdir(scrsht)
	for i in ls:
		if(i[-4:]==".png"):
			if(i not in arr):
				shutil.copyfile(scrsht+'\\'+i,backup+'\\'+i)
				os.rename(scrsht+'\\'+i,scrsht+'\\'+"img.png")
				image = "telegram-send --image {}\\img.png".format(scrsht)
				sp.call(image)
				os.remove(scrsht+'\\img.png')
	# break