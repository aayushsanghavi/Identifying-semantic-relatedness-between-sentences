import re
import sys
import csv
import random
from nltk import word_tokenize

data = []
infile = sys.argv[1]

with open(infile, "r") as file:
	reader = csv.reader(file, delimiter=',')
	for row in reader:
		sentence1 = row[2] + ". " + row[4]
		sentence1 = re.sub(r"[^\x00-\x7F]+", " ", sentence1)
		tokens = word_tokenize(sentence1)
		sentence1 = " ".join(tokens)
		sentence2 = row[3]+". "+row[5]
		sentence2 = re.sub(r"[^\x00-\x7F]+", " ", sentence2)
		tokens = word_tokenize(sentence2)
		sentence2 = " ".join(tokens)
		instanceID = int(row[0]+row[1])
		line = [1, sentence1, sentence2, instanceID]
		data.append(line)

random.shuffle(data)
test_data = data[:10000]
dev_data = data[10000:20000]
train_data = data[20000:]

with open("train.tsv", "w") as file:
	writer = csv.writer(file, delimiter='\t')
	for row in train_data:
		writer.writerow(row)

with open("test.tsv", "w") as file:
	writer = csv.writer(file, delimiter='\t')
	for row in test_data:
		writer.writerow(row)

with open("dev.tsv", "w") as file:
	writer = csv.writer(file, delimiter='\t')
	for row in dev_data:
		writer.writerow(row)