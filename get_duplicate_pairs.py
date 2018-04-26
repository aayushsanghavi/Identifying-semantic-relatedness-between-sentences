import sys
import numpy as np
import xml.etree.cElementTree as ET

args = sys.argv
infile = args[1]
outfile = args[2]
duplicate_pairs = []

context = ET.iterparse(infile, events=("start", "end"))
context = iter(context)
event, root = context.next()
duplicate_count = 0

for event, elem in context:
	if event == "end" and elem.tag == "row":
		linktype = int(elem.get("LinkTypeId"))
		if linktype == 3:
			duplicate_count += 1
			original_post_id = int(elem.get("RelatedPostId"))
			duplicate_post_id = int(elem.get("PostId"))
			duplicate_pairs.append((original_post_id, duplicate_post_id))
		if root:
			root.clear()
		elem.clear()

print duplicate_count
np.save(outfile, np.asarray(duplicate_pairs))