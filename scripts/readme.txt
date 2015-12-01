Read me

1. Map to reference (reference proteome, saving directory, path to the snap2 files)
#Command:
	python .../mapSnap2ToReference.py -i .../UP000002241_11706.fasta -d ~/test -s ~/test/11706/split/snap2


#Output files looks like mappedRefProteome... (one has only the headers, the other file contains all mapped sequences)
2. Get Keys (as commandline parameter u need the already mapped headers, saving directory)
#Command:
	python .../scripts/getKeys.py -i .../mappedRefProteome_headers.fasta1448970641.23 -d ~/test

#Output file looks like - keys....

3. Count Keywords (as commandline parameter u need the .tab file from uniprot, saving directory)
#Command:

	python .../scripts/countKeywords.py -i .../strong_high_keywords_uniprot_tab -d ~/test

#Output file looks like - countKeywordsDataFile...

! Set -d for 1,2,3 the same...then u will have everything in 1 place
! Ignore files with name aux...
! 

