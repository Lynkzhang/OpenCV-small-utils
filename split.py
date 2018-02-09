#!/bin/python

import cv2
import numpy
import os

filedir='your/file/dir/' # make sure this ended with '/'

def file_name(file_dir): # get all dir of pics and return them in a list
	L=[]   
	for root, dirs, files in os.walk(file_dir):  
		for file in files:  
			if os.path.splitext(file)[1] == '.jpg': 
				L.append(os.path.join(root, file))  
	return L

if not os.path.exists(filedir+"r/"):
  os.makedirs(filedir+"r/")
if not os.path.exists(filedir+"g/"):
  os.makedirs(filedir+"g/")
if not os.path.exists(filedir+"b/"):
  os.makedirs(filedir+"b/")


pics=file_name(filedir)
for i in pics:
	img = cv2.imread(i)
	b,g,r = cv2.split(img)
	picname=i.split("/")[-1] #find file name
	cv2.imwrite(filedir+"r/"+picname, r)
	cv2.imwrite(filedir+"g/"+picname, g)
	cv2.imwrite(filedir+"b/"+picname, b)
  
  
  
