#!/usr/bin/Python

import os

# Convert mappedIDToKeywords
os.popen("rm onlyKeywords.out")
os.popen("cut -f 2- mappedIDToKeywords.tab | tail -n +2 > onlyKeywords.out")

# Dictionary with keywords
keywordsDict = {}

file = open('onlyKeywords.out','r')

for line in file:
	lineArray = line.split(";")
	for k in lineArray:
		print k
		if len(k) > 0:
			if k in keywordsDict:
				keywordsDict[k] +=1
			else:
				keywordsDict[k] = 1

file.close()

# Save counted keys in file
writeFile = open('countKeywordsDataFile.out','w')
for k in keywordsDict:
	writeFile.write(k+"\t"+str(keywordsDict[k])+"\n")

writeFile.close()	

os.system("cat countKeywordsDataFile.out | sort -k2 -n | tail -10 > top10Keys.out")




