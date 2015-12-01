#!/usr/bin/Python

# Map SNAP2 Predictions to a given reference proteome
import os
import re
import sys
import time

filePath = "ftp://ftp.ebi.ac.uk/pub/databases/reference_proteomes/QfO/Eukaryota/UP000005640_9606.fasta.gz"
flagWget = False
homeDir = "./"
snapFileDir = "/mnt/project/tmhpred/willbebig/snap2/"

try:
 	opts, args = getopt.getopt(argv,"hwi:dir",["ifile=","help=","wget=","directory="])
except getopt.GetoptError:
 	print 'skript.py -i <input file path> -w[option - file should have .gz extension] -dir <homeDirectory>'
 	sys.exit(2)
for opt, arg in opts:
	if opt in ("-h","--help"):
    	print 'skript.py -i <input file with absolute path> -w[option - file should have .gz extension] -dir <homeDirectory>'
    	sys.exit()
	elif opt in ("-i", "--ifile"):
		filePath = arg
	elif opt in ("-w", "--wget"):
		flagWget = True
	elif opt in ("-dir", "--directory"):
    	homeDir = arg
	

# Get Reference Proteome file
fileRefArray = []
if flagWget == True:
	filesRef = os.popen("wget -qO- "+hostDir+" | gunzip").read()
	fileRefArray = filesRef.split('>')
else:
	in = open(filePath,'r')
	

dict = {}

# Build Dictionary for the Reference Proteome file

if flagWget == True: # File downloaded via ftp
	for i in fileRefArray:
		myhash = i.split('\n',1)
		if(len(myhash) == 2 and len(myhash[0])>0):
			dict['>'+myhash[0]]=[myhash[1].replace("\n",""),0] 
else: # File read via absolute path
	id = ""
	seq = ""
	while in.readline() as aux:
		if '>' in aux:
			if len(seq) > 0:
				dict[id]=[seq,0]
			id = aux
			seq = ""
		else:
			seq += aux 
	
########################## Get .snap2 Files ############################

filesSnap = os.popen("ls -1 "+snapFileDir+" | awk '$1 ~ /snap2/ && $1 ~ /UP0/ {print}'").read()
fileSnapArray = filesSnap.split('\n')

# Map snap2 over Reference Proteome
print "start match"
for i,item in enumerate(fileSnapArray):
	if len(item)>0:
		print i
		myseq = os.popen("cat "+item+" | awk '{print $1}' | uniq |awk '{print substr($1,0,length($1)-1)}' | uniq |awk '{print substr($1,0,1)}' | paste -s -d \"\"").read()
		myseq = myseq.replace("\n","")
		for keySeq in dict:
			if myseq in dict[keySeq][0]:
				dict[keySeq][1] += 1 
		
filesSnap.close()

# Map snap2 over Reference Proteome
print "start match"
for i,item in enumerate(fileSnapArray):
	if len(item)>0:
		print i
		myseq = os.popen("cat "+item+" | awk '{print $1}' | uniq |awk '{print substr($1,0,length($1)-1)}' | uniq |awk '{print substr($1,0,1)}' | paste -s -d \"\"").read()
		myseq = myseq.replace("\n","")
		for keySeq in dict:
			if myseq in dict[keySeq][0] :
				dict[keySeq][1] += 1 

######## Print how many sequence matching for .SNAP2 ########

dimRefProteome = len(dict)

# Filter Ref Proteome dict - only the matches will remain

fastaIDArray = filter(lambda x:dict[x][1]>0, dict) # Fasta IDs for the already gemapped sequences
print "Total mapped sequnces: " + str(len(fastaIDArray))
print "Not mapped: " + str(dimRefProteome - len(fastaIDArray))

#### Print into File the mapped reference proteome (only for .SNAP2)#####

target = open(homeDir + str(time.time())+"mappedRefProteome.fasta','w')
for key in fastaIDArray:
	if dict[key][1]>0:
		target.write(key)
		target.write("\n")
		target.write(dict[key][0])
		target.write("\n")

target.close()


target = open(homeDir + str(time.time()) + 'mappedRefProteome_keys.fasta','w')
for key in fastaIDArray:
	target.write(key)
	target.write("\n")

target.close()
print "finally done"


 
    



	

