import cv2
import numpy
import os
import sys, getopt
from skimage import data
from skimage import filters
from skimage import exposure



def file_name(file_dir): # get all dir of pics and return them in a list
	L=[]   
	for root, dirs, files in os.walk(file_dir):  
		for file in files:  
			if os.path.splitext(file)[1] == '.jpg': 
				L.append(os.path.join(root, file))  
				if not os.path.exists("./"+ root.split("/")[-1] +"_seg/"):
  					os.makedirs("./"+ root.split("/")[-1] +"_seg/")
	return L

def main(argv):
	bias = -50
	filedir='/default/path/' # make sure this ended with '/'
	
	try:
		opts, args = getopt.getopt(argv,"hi:b:",["ifile=","bias="])
	except getopt.GetoptError:
		print ('seg.py -i <inputfile> -b <bias>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print ('seg.py -i <inputfile> -b <bias>')
			sys.exit()
		elif opt in ("-i", "--input"):
			filedir = arg
		elif opt in ("-b", "--bias"):
			bias = int(arg)

	processing(bias,filedir)

def processing(bias=-50,filedir='/default/path/'):
	
	pics=file_name(filedir)

	print ("processing dir is %s"%filedir)
	print ("processing with bias %d"%bias)

	for i in pics:
		picname=i.split("/")[-1]
		img = cv2.imread(i)
	#	b,g,r = cv2.split(img)
		gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY);
	#	thres = filters.threshold_otsu(b)
		thres = filters.threshold_otsu(gray)
		bin = cv2.threshold(gray,thres+bias,255,cv2.THRESH_BINARY)
	#	bin = cv2.threshold(b,thres,255,cv2.THRESH_BINARY)
		mask=bin[1]
		cv2.bitwise_not(mask,mask)
		masked = cv2.bitwise_and(img,img,mask=mask)
		cv2.imwrite(i.split("/")[-2]+"_seg/"+picname, masked)


if __name__ == "__main__":
	main(sys.argv[1:])
