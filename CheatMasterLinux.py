import subprocess as sp
import os
import sys

scrsht = str(sys.argv[1])

arr = []

while(1):
	ls = os.listdir(scrsht)
	for i in ls:
		image = scrsht+i
		if(i not in arr):
			sp.call(["telegram-send","--image","{}".format(image)])
			print(image,"Sent!")
			arr.append(i)
