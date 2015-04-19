# Code explaination: http://ilearnblogger.blogspot.tw/2015/04/qnaplinux-python-programming-02-basic.html
#!/usr/bin/python

# import sys; fn = raw_input("Input file name: "); file = open(fn, "r"); print file.read()
# import sys; file = open(sys.argv[1], "r"); print file.read()

import sys, getopt

if getopt.getopt(sys.argv, "-f"):
	fn = getopt.getopt(sys.argv, "-f")
	print fn
	try:
	  file = open(fn, "r") # open existed file with "w" may empty the file
	except IOError:
	  print "There was an error reading to", fn
	  sys.exit()
	print file.read()
print "End"
