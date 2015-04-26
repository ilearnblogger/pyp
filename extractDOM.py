# Code explaination: Parse HTML and Extract texts defined in some XPath
# http://ilearnblogger.blogspot.tw/2015/04/qnaplinux-python-programming-04-learn.html
#!/usr/bin/python

import urllib3
from bs4 import BeautifulSoup

http = urllib3.PoolManager()
r = http.request('GET', 'http://ilearnblogger.blogspot.tw/2014/01/office-onenote.html')

soup = BeautifulSoup(r.data)
items = soup.select(".post-labels")
tags = []
for item in items: 
	for links in item.find_all('a'): 
		tags.append(links.string.strip())
print tags
for s in tags: print s