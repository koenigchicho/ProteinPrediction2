#!/usr/bin/Python

# Get all keys from .fasta files
import os
import re

######################################################## Get .fasta Files ##################################################################################################
dir = "/mnt/project/tmhpred/willbebig/snap2"
filesSnap = os.popen("ls -1 " + dir + " | awk '$1 !~ /snap2/ && $1 ~ /UP0/ {print}'").read()
fileSnapArray = filesSnap.split('\n')


######################################################## Get fastaID ##################################################################################################
target = open('/mnt/home/student/mgiurgiu/protein_prediction/ProteinPrediction2/SNPs/fastaID.out','w')

for i,item in enumerate(fileSnapArray):
	if len(item)>0:
		print i
		myhead = os.popen("head -n 1 "+dir+"/"+item+" | awk '{print $1}'").read()
		myhead = myhead.replace("\n","")
		print myhead
		key = (myhead.split("|"))[1]
		target.write(key+" ")
target.close()
