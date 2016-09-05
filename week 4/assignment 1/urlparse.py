import urllib2 as irl
from bs4 import BeautifulSoup as bs

html = irl.urlopen('http://python-data.dr-chuck.net/comments_184702.html').read()
soup = bs(html)
tags = soup('span')
c = 0
for tag in tags:
    c += int(tag.contents[0])
print c
