#!/usr/bin/Python
# Get all keys from .fasta files
import os
import re
import sys

######################################################## Get .fasta Files ##################################################################################################
dirServer = "/mnt/project/tmhpred/willbebig/snap2"

# To set
homeDir = "./"
outFileName = "fastaID.out"

try:
 	opts, args = getopt.getopt(argv,"hdir:o:",["directory=","ofile=","help="])
except getopt.GetoptError:
 	print 'getKeys.py -dir <homeDirectory> -o <outputfile>'
 	sys.exit(2)
for opt, arg in opts:
	if opt in ("-h","--help"):
    	print 'getKeys.py -dir <homeDirectory> -o <outputfile>'
    	sys.exit()
	elif opt in ("-dir", "--directory"):
    	homeDir = arg
	elif opt in ("-o", "--ofile"):
		outFileName = arg

filesSnap = os.popen("ls -1 " + dirServer + " | awk '$1 !~ /snap2/ && $1 ~ /UP0/ {print}'").read()
fileSnapArray = filesSnap.split('\n')
filesSnap.close()

######################################################## Get fastaID ##################################################################################################
target = open(homeDir+outFileName,'w')

for i,item in enumerate(fileSnapArray):
	if len(item)>0:
		print i
		myhead = os.popen("head -n 1 "+item+" | awk '{print $1}'").read()
		myhead = myhead.replace("\n","")
		key = myhead.split("|")[1]
		targe.write(key+" ")
target.close()




 
    



	

