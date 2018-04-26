import re
import csv
import random
from nltk import word_tokenize

data = []
infile = "stackoverflow_non_duplicate_questions.tsv"

with open(infile, "r") as file:
	reader = csv.reader(file, delimiter='\t')
	for row in reader:
		sentence1 = row[1]
		sentence1 = re.sub(r"[^\x00-\x7F]+", " ", sentence1)
		tokens = word_tokenize(sentence1)
		sentence1 = " ".join(tokens)
		sentence2 = row[2]
		sentence2 = re.sub(r"[^\x00-\x7F]+", " ", sentence2)
		tokens = word_tokenize(sentence2)
		sentence2 = " ".join(tokens)
		label = int(row[0])
		instanceID = int(row[3])
		line = [label, sentence1, sentence2, instanceID]
		data.append(line)

random.shuffle(data)
test_data = data[:10000]
dev_data = data[10000:20000]
train_data = data[20000:]

with open("train.tsv", "a") as file:
	writer = csv.writer(file, delimiter='\t')
	for row in train_data:
		writer.writerow(row)

with open("test.tsv", "a") as file:
	writer = csv.writer(file, delimiter='\t')
	for row in test_data:
			writer.writerow(row)

with open("dev.tsv", "a") as file:
	writer = csv.writer(file, delimiter='\t')
	for row in dev_data:
		writer.writerow(row)