import re
import sys
import gc
import numpy as np
import HTMLParser as HP
from bs4 import BeautifulSoup
import xml.etree.cElementTree as ET

reload(sys)
sys.setdefaultencoding('utf-8')

args = sys.argv
p = HP.HTMLParser()
posts_infile = args[1]
words_file = args[2]
words = {}
count = 0

context = ET.iterparse(posts_infile, events=("start", "end"))
context = iter(context)
event, root = context.next()
for event, elem in context:
	if event == "end" and elem.tag == "row":
		post_type = int(elem.get("PostTypeId"))
		if post_type == 1:
			count += 1
			content = elem.get("Title") + elem.get("Body")
			content = content.decode().encode("utf-8")
			try:
				content = p.unescape(content)
				content = BeautifulSoup(content, "lxml")
				content.pre.decompose()
				content = content.get_text("\n").strip()
				content = re.sub(r"[\n]+", " ", content)
				content = re.sub(r"[^\x00-\x7F]+", " ", content)
				content = content.split()
				for word in content:
					word = word.lower()
					word = re.sub(r"[^a-z0-9]+", "", word)
					l = len(word)
					if l > 1 and l < 13:
						words[word] = True
			except:
				pass

			if count % 50000 == 0:
				gc.collect()

		elem.clear()
		if root:
			root.clear()

out_file = open(words_file, "w")
for word in words:
	word += "\n"
	out_file.write(word)
out_file.close()