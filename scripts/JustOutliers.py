#!/usr/bin/python


# To set
idfile = "/home/fabian/Projects/ProteinPrediction2/ids/ids/3702.neutral.txt"
keywordsfile = "/home/fabian/Projects/ProteinPrediction2/kw_mapping/3702_kw_all.tab"
outfile = "/home/fabian/Projects/ProteinPrediction2/kw_mapping/3702_kw_neutral.tab"

with open(idfile, 'r') as f:
    ids = f.read().splitlines()

with open(keywordsfile, 'r')as f:
    keywords = f.read().splitlines()

with open(outfile, 'w') as out:
    out.write(keywords[0] + '\n')
    for k in keywords:
        if k.startswith(tuple(ids)):
            out.write(k + '\n')