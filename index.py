import sys, os, pprint

'''
author: jose reyes
  date: 01/23/22
  desc: Creates inverted index of files in a given directory. 
        Often inverted indices are used to create search programs.
  vers: 1.0
'''

# No argument given
if len(sys.argv) < 2:
    print('No directory was given.')
    print('Usage: python3 index.py <directory>')
    quit()

wd = sys.argv[1] # working directory

d = {}  # dictionary (inverted index)
dc = 0  # document

for record in os.listdir(wd):
    if record.endswith('.py'):
        continue

    dc+=1
    doc = open(record, 'r')
    for line in doc:
        l = line.split()
        for term in l:
            if term not in d:
                d[term]=[]
                d[term].append(1)
                d[term].append([record])
            else:
                d[term][0]+=1
                d[term][1].append(record)
pprint.pprint(d)
