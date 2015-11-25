#!/usr/bin/Python

import os

filesSnap = os.popen("ls -1 /mnt/project/tmhpred/willbebig/snap2/ | awk '$1 ~ /snap2/ && $1 ~ /UP0/ {print}'").read()
fileSnapArray = filesSnap.split('\n')

out = os.open('/mnt/home/student/aberatis/outputTest','w',)
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