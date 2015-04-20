# Code explaination: http://ilearnblogger.blogspot.tw/2015/04/qnaplinux-python-programming-01-setup.html
#!/usr/bin/python

import urllib3

http = urllib3.PoolManager()
r = http.request('GET', 'http://ilearnblogger.blogspot.tw/2015/04/qnaplinux-python-programming-01-setup.html')
print r.status, r.data