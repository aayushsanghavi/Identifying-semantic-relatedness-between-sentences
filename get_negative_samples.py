import csv
import sys
import random

ids = []
pairs = {}
questions = {}
infile = sys.argv[1]

with open(infile, "r") as file:
	reader = csv.reader(file, delimiter=',')
	for row in reader:
		id1 = row[0]
		id2 = row[1]
		if id1 not in pairs:
			ids.append(id1)	
			pairs[id1] = []
		if id2 not in pairs:
			ids.append(id2)
			pairs[id2] = []
		pairs[id1].append(id2)
		pairs[id2].append(id1)
		sentence1 = row[2]+". "+row[4]
		sentence2 = row[3]+". "+row[5]
		questions[id1] = sentence1
		questions[id2] = sentence2

x = len(ids)
outfile = open("stackoverflow_non_duplicate_questions.tsv", "w")
writer = csv.writer(outfile, delimiter='\t')
for i in range(365000):
	a = random.randint(0, x-1)
	a = ids[a]
	b = random.randint(0, x-1)
	b = ids[b]
	if b not in pairs[a] and a not in pairs[b]:
		row = [0, questions[a], questions[b], int(a+b)]
		writer.writerow(row)
outfile.close()