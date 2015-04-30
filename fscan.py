# Code explaination: Scan file systems and Extract metadata and texts from files
#!/usr/bin/python
import sys, getopt, os
from urlparse import urlparse
# import psycopg2
import psycopg2, psycopg2.extras

def main(argv):
  parseArgs()

def dbConn():
  conn = psycopg2.connect("dbname=fbi user=nas password=QNAP.csie")
  cur = conn.cursor()
  cur.execute("SELECT * FROM Object;")
  cur.fetchone()

def addRepository(arg):
  r = urlparse(arg)
  if os.path.isdir(arg): # local directory exists!
    print "Local dir exists. " + os.path.abspath(arg)
    insertDbResp('file', 'localhost', os.path.abspath(arg))
  elif r.netloc == '': # not remote path --> dir not exist!
    print "Local dir does not exist!"
  else: # remote repositiry
    print arg + " Not supported now!"

def insertDbResp(scheme, host, path):
  print scheme + '://' + host + path

# print os.listdir(arg)


def parseArgs():
  try: opts, args = getopt.getopt(sys.argv[1:], 'r:s:h')
  except getopt.GetoptError as err: print str(err); exit(0)

  for opt, arg in opts:
    if opt == '-r': addRepository(arg)
    if opt == '-s':
      if arg == None: arg = 1
      print "scanDir(int(arg)): " + arg
    if opt == '-h': printHelp()

def printHelp():
  print '''
  fscan: File Scanner
  -- Set the entry point for scanning some folder of a file system
  -- Store the root directory tree info. into PostgreSQL database
    (support local file system and SAMBA file system)
  Option:
    -r [Repository]: Add repository to database as the initial task
    -s [number]: Scan (-s: breadth first search) [number] folders and their files 
    -h: Help
  '''

if __name__ == "__main__": main(sys.argv[1:])