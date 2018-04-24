import cv2
import numpy
import os
from skimage import data
from skimage import filters
from skimage import exposure

filedir='/Path/tp/your/dir/' # make sure this ended with '/'

def file_name(file_dir): # get all dir of pics and return them in a list
	L=[]   
	for root, dirs, files in os.walk(file_dir):  
		for file in files:  
			if os.path.splitext(file)[1] == '.jpg': 
				L.append(os.path.join(root, file))  
	return L

if not os.path.exists(filedir+"seg/"):
  os.makedirs(filedir+"seg/")

pics=file_name(filedir)
for i in pics:
	picname=i.split("/")[-1]
	img = cv2.imread(i)
#	b,g,r = cv2.split(img)
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY);
#	thres = filters.threshold_otsu(b)
	thres = filters.threshold_otsu(gray)
	bin = cv2.threshold(gray,thres,255,cv2.THRESH_BINARY)
#	bin = cv2.threshold(b,thres,255,cv2.THRESH_BINARY)
	mask=bin[1]
	cv2.bitwise_not(mask,mask)
	masked = cv2.bitwise_and(img,img,mask=mask)
	cv2.imwrite(filedir+"seg/"+picname, masked)
