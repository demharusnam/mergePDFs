#!/usr/bin/env python

''' 
	mergePDFs.py - merges all PDFs inputted into a single document

	Accepts input parameters as command line arguments (argv). Optional last argument 
	can be used to create custom output file name. If used, last argument must NOT have .pdf at the end of outputfile name.

	e.g. (macOS) 

	python mergePDFs.py first_file.pdf second_file.pdf third_file.pdf output_filename


	OR since I added the shebang at the top of the file you could run it as such:


	./mergePDFs.py first_file.pdf second_file.pdf third_file.pdf output_filename

	However, that may give a "permission denied" error. To add execution permission, do the following
	and retry the above commands:

	chmod +x mergePDFs.py
'''

from sys import argv
from PyPDF4 import PdfFileMerger

FLAG_HELP = {"-h", "--help"}
USAGE = """\
Merges PDF documents input from the command line.
%(program_name)s: [PDF Files] [output filename]
%(program_name)s: [-h | --help]
""" % {"program_name": argv[0]}

def main():
	output = "PyPDF-Merging-Output.pdf"

	if set(argv) & FLAG_HELP:
		print(USAGE)
		exit(0)
	elif len(argv) < 2:
		print(USAGE)
		exit(1)
	else:
		files = [f.strip() for f in argv[1:len(argv)-1]]

		if '.pdf' not in argv[len(argv)-1]:
			output = argv[len(argv)-1].strip() + '.pdf'

	merger = PdfFileMerger()

	for file in files:
		input_file = open(file,"rb")
		merger.append(fileobj=input_file)

	merger.write(open(output,"wb"))
	merger.close()


if __name__ == "__main__":
	main()


