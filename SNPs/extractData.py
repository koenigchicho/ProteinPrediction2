#!/usr/bin/Python

import os
import sys

dirHome = "./"
outFileName = ""
dirServer = "/mnt/project/tmhpred/willbebig/snap2/"

try:
 	opts, args = getopt.getopt(argv,"hdir:o:",["directory=","ofile=","help="])
except getopt.GetoptError:
 	print 'extractData.py -dir <homeDirectory> -o <outputfile>'
 	sys.exit(2)
for opt, arg in opts:
	if opt in ("-h","--help"):
    	print 'extractData.py -dir <homeDirectory> -o <outputfile>'
    	sys.exit()
	elif opt in ("-dir", "--directory"):
    	dirHome = arg
	elif opt in ("-o", "--ofile"):
		outFileName = arg

#Read every .snap2 file
filesSnap = os.popen("ls -1 "+dirServer+" | awk '$1 ~ /snap2/ && $1 ~ /UP0/ {print}'").read()
fileSnapArray = filesSnap.split('\n')

out = os.open(dirHome+outFileName,'w',)
# Map snap2 over Reference Proteome
print "start match"
for i,item in enumerate(fileSnapArray):
    if len(item)>0:
            print i
            myseq = os.popen("cat "+item+" | awk '{if($2 ~ /=>/) {printf (\"%s\t%s\t\",$1,$35)} else if($2 !~ /=>/) {printf (\"%s\t%s\n\",$2,$4)}}'").read()
            myseq = myseq.replace("\n","")
            out.write(myseq)
            for keySeq in dict:
                if myseq in dict[keySeq][0]:
                    dict[keySeq][1] += 1
out.close()
