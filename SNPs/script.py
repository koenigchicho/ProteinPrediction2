#!/usr/bin/Python

#ls -1 | awk '$1 !~ /snap2/ && $1 ~ /UP0/ {print}'
#cat UP000005640_9606_sing.fasta20877.snap2 | awk '{print $1}' | uniq |awk '{print substr($1,0,length($1)-1)}' | uniq |awk '{print substr($1,0,1)}' | paste -s -d "" 

import os

# Get Reference Proteome file
filesRef = os.popen("wget -qO- ftp://ftp.ebi.ac.uk/pub/databases/reference_proteomes/QfO/Eukaryota/UP000005640_9606.fasta.gz | gunzip").read()
fileRefArray = filesRef.split('>')

dict = {}

# Build Dictionary for the Reference Proteome file
for i in fileRefArray:
	myhash = i.split('\n',1)
	if(len(myhash) == 2 and len(myhash[0])>0):
		dict['>'+myhash[0]]=[myhash[1].replace("\n",""),0] 

# Get .snap2 Files
filesSnap = os.popen("ls -1 | awk '$1 ~ /snap2/ && $1 ~ /UP0/ {print}'").read()
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
		
# Get .fasta Files - Test if one of the proteins seq mapp directly to Reference proteome

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

######## Print how many sequence matching  ########

dimRefProteome = len(dict)

# Filter Ref Proteome dict - only the matches will remain

fastaIDArray = filter(lambda x:dict[x][1]>0, dict) # Fasta IDs for the already gemapped sequences

print "Total mapped sequnces: " + str(len(fastaIDArray))

print "Not mapped: " + str(dimRefProteome - len(fastaIDArray))

#### Print into File the mapped reference proteome #####

targe = open('mappedRefProteome.fasta','w')


for key in dict:
	if dict[key][1]>0:
		target.write(key)
		target.write("\n")
		target.write(dict[key][0])

print "finally done"
target.close()

 
    



	

