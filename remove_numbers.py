import sys

word_file = sys.argv[1]
outfile = word_file + "_cleaned"

file = open(word_file, "r")
out = open(outfile, "w")
for line in file:
	try:
		x = float(line.strip())
	except:
		out.write(line)

file.close()
out.close()