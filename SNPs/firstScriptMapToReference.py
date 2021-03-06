#!/usr/bin/Python

#calling only on SNAP2 Data
#
#>>> print "Total mapped sequnces: " + str(len(fastaIDArray))
#Total mapped sequnces: 20667
#>>> 
#>>> print "Not mapped: " + str(dimRefProteome - len(fastaIDArray))
#Not mapped: 215

#calling with SNAP2 Data and .fasta
#
#>>> print "Total mapped sequnces: " + str(len(fastaIDArray))
#Total mapped sequnces: 20882
#>>> 
#>>> print "Not mapped: " + str(dimRefProteome - len(fastaIDArray))
#Not mapped: 0
#>>> 

######## Ignore X position
# Total mapped sequnces: 20827
# Not mapped: 55



import os
import re
import sys

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
	
######################################################## Get .snap2 Files ##################################################################################################

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

# Map snap2 over Reference Proteome -Ignore X in reference (allow mismatch)
print "start match"
for i,item in enumerate(fileSnapArray):
	if len(item)>0:
		print i
		myseq = os.popen("cat "+item+" | awk '{print $1}' | uniq |awk '{print substr($1,0,length($1)-1)}' | uniq |awk '{print substr($1,0,1)}' | paste -s -d \"\"").read()
		myseq = myseq.replace("\n","")
		for keySeq in dict:
			if myseq in dict[keySeq][0] :
				dict[keySeq][1] += 1 
			else:
				if len(myseq)==len(dict[keySeq][0]):
					flag = 1
					mismatchPosition = [i for i,(a1,b1) in enumerate(zip(myseq,dict[keySeq][0])) if b1 != a1]
					for pos in mismatchPosition:
						if dict[keySeq][0][pos] != 'X':
							flag = 0
							break
					if flag == 1:
						dict[keySeq][1] += 1 
					

######## Print how many sequence matching only for .SNAP2 ########

dimRefProteome = len(dict)

# Filter Ref Proteome dict - only the matches will remain

fastaIDArray = filter(lambda x:dict[x][1]>0, dict) # Fasta IDs for the already gemapped sequences
print "Total mapped sequnces: " + str(len(fastaIDArray))
print "Not mapped: " + str(dimRefProteome - len(fastaIDArray))

#### Print into File the mapped reference proteome (only for .SNAP2)#####

target = open(homeDir + str(time.time())+"mappedRefProteomeAllowMismatchX.fasta','w')
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

################################ Get .fasta Files - Test if one of the proteins seq mapp directly to Reference proteome ###############################################################

filesFasta = os.popen("ls -1 | awk '$1 !~ /snap2/ && $1 ~ /UP0/ {print}'").read()
fileFastaArray = filesFasta.split('\n')

for i,item in enumerate(fileFastaArray):
	if len(item)>0:
		print i
		myseq = os.popen("cat "+item).read()
		# skip header
		myseq = myseq.split("\n",1)[1]
		# make one long string
		myseq = myseq.replace("\n","")
		for keySeq in dict:
			if myseq in dict[keySeq][0]:
				dict[keySeq][1] += 1 
	
filesFasta.close()

fastaIDArray = filter(lambda x:dict[x][1]>0, dict) # Fasta IDs for the already gemapped sequences
print "Total mapped sequnces: " + str(len(fastaIDArray))
print "Not mapped: " + str(dimRefProteome - len(fastaIDArray))

#### Print into File the mapped reference proteome (only for .SNAP2)#####

target = open('/mnt/home/student/mgiurgiu/protein_prediction/ProteinPrediction2/SNPs/mappedRefProteome_total.fasta','w')

for key in fastaIDArray:
	if dict[key][1]>0:
		target.write(key)
		target.write("\n")
		target.write(dict[key][0])


target.close()


######################### Compare #########################

files = os.popen("ls -1 | awk '$1 !~ /snap2/ && $1 ~ /UP0/ {print}'").read()
fileArray = files.split('\n')
dictSeq = {}
for i,item in enumerate(fileArray):
	if len(item)>0:
		myseq = os.popen("cat "+item).read()
		# skip header
		myseqArr = myseq.split("\n")
		# make one long string
		id = myseqArr[0].replace("\n","")
		seq = myseqArr[1].replace("\n","")
		dictSeq[id]=seq
files.close()

out = open('/mnt/home/student/mgiurgiu/protein_prediction/ProteinPrediction2/SNPs/differences.fasta','w')
for key in dict:
	if dict[key][1] == 0:
		out.write(key+'\n')
		out.write(dict[key][0]+'\n\n')
		out.write(dictSeq[key]+'\n\n\n')

out.close()		

print "finally done"


 
    



	

