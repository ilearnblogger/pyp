# Code explaination: Scan file systems and Extract metadata and texts from files
#!/usr/bin/python
import sys, getopt, os, time
from urlparse import urlparse
import psycopg2, psycopg2.extras

def main(argv):
  dbConn()
  parseArgs()
  conn.close()

def dbConn():
  global conn, cur
  conn = psycopg2.connect("host=localhost dbname=fs user=nas")
  cur = conn.cursor()

def addRepository(arg):
  r = urlparse(arg)
  if os.path.isdir(arg): # local directory exists!
    print "Local dir exists. " + os.path.abspath(arg)
    (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(arg)
    print (mode, ino, dev, nlink, uid, gid, size, time.ctime(atime), time.ctime(mtime), time.ctime(ctime))
    insertDbResp('file', 'localhost', os.path.abspath(arg), mtime)
  elif r.netloc == '': # not remote path --> dir not exist!
    print "Local dir does not exist!"
  else: # remote repositiry
    print arg + " Not supported now!"

def insertDbResp(scheme, host, path, dt):
  global repCID
  repCID = 2
  s = path.split("/")
  name = s[len(s) - 1]
  sql = (repCID, name, time.ctime(dt), scheme, host, path)
  sql = "select InsertClassFS" + str(sql) + ";"
  print sql
  cur.execute(sql)
  print "Added CID was " + str(cur.fetchone())
  conn.commit() # db transaction will be completed after commit()

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