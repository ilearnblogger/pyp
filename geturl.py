# Code explaination: http://ilearnblogger.blogspot.tw/2015/04/qnaplinux-python-programming-01-setup.html
#!/usr/bin/python

import urllib
urls=('http://ilearnblogger.blogspot.tw/2015/04/qnaplinux-tool-postgresql-from-9210.html','http://ilearnblogger.blogspot.tw/2015/03/qnaplinux-tool-postgresql-database.html')
i = 0
for url in urls:
  file_path = './urls/' + str(i)
  urllib.urlretrieve (url, file_path)
  i = i+1

