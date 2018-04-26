import re
import gc
import sys
import csv
import numpy as np
import HTMLParser as HP
from bs4 import BeautifulSoup
import xml.etree.cElementTree as ET
reload(sys)
sys.setdefaultencoding('utf-8')

titles = {}
body = {}
count = 0
args = sys.argv
p = HP.HTMLParser()
posts_infile = args[1]
duplicate_pairs_infile = args[2]
duplicate_pairs_outfile = args[3] + ".tsv"

duplicate_pair_ids = np.load(duplicate_pairs_infile)
for pair in duplicate_pair_ids:
	original, duplicate = pair
	original = int(original)
	duplicate = int(duplicate)
	titles[original] = "NA"
	body[original] = "NA"
	titles[duplicate] = "NA"
	body[duplicate] = "NA"

context = ET.iterparse(posts_infile, events=("start", "end"))
context = iter(context)
event, root = context.next()
for event, elem in context:
	if event == "end" and elem.tag == "row":
		post_type = int(elem.get("PostTypeId"))
		if post_type == 1:
			count += 1
			post_id = int(elem.get("Id"))
			if post_id in titles:
				title = elem.get("Title").encode("utf-8").strip()
				content = elem.get("Body").decode().encode("utf-8").strip()
				content = p.unescape(content)
				try:
					content = BeautifulSoup(content, "lxml")
					try:
						content.pre.decompose()
					except:
						pass
					content = content.get_text("\n").strip()
					content = re.sub(r"[\n]+", " ", content)
					content = re.sub(r"[^\x00-\x7F]+", " ", content)
					content = re.sub(r'Possible Duplicate: ', "", content)
					content = re.sub(r'See: ', "", content)
					content = content.strip()
					titles[post_id] = title
					body[post_id] = content
				except:
					pass

			if count % 50000 == 0:
				gc.collect()

		elem.clear()
		if root:
			root.clear()

outfile = open(duplicate_pairs_outfile, "w")
writer = csv.writer(outfile, delimiter=',')
for pair in duplicate_pair_ids:
	original, duplicate = pair
	original = int(original)
	duplicate = int(duplicate)
	if titles[original] != "NA" and titles[duplicate] != "NA":
		writer.writerow([original, duplicate, titles[original], titles[duplicate], body[original], body[duplicate]])
outfile.close()