# Code explaination: http://ilearnblogger.blogspot.tw/2015/04/qnaplinux-python-programming-03-command.html
#!/usr/bin/python
import sys, getopt

def msg(errarg):
	if errarg: print errarg
	print 'xxx.py -f <inputfile>'
	print 'xxx.py -h or --help'
	print 'xxx.py -v or -version'

def main(argv):
	inputfile = ''
	try:
	  opts, args = getopt.getopt(argv, "hvrwf:", ["help","version","file="])
	  # print opts, args
	except getopt.GetoptError:
		msg("Error args!"); sys.exit(2)
	
	for opt, arg in opts:
	  if opt in ("-h", "--help"):
	     msg("Help: "); sys.exit()
	  elif opt in ("-v", "--version"):
	     print 'xxx.py ver 0.1'; sys.exit()
	  elif opt in ("-r", "-w"):
	     print "Open file with:", opt
	  elif opt in ("-f", "--file"):
	     inputfile = arg
	print 'Input file is:', inputfile

if __name__ == "__main__": main(sys.argv[1:])
