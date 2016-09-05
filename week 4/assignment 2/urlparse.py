import urllib2 as irl
from bs4 import BeautifulSoup as bs

url = 'http://python-data.dr-chuck.net/known_by_Peyton.html'
pos = 18
repeat = 7
while repeat>0:
    html = irl.urlopen(url).read()
    soup = bs(html)
    tags = soup('a')[pos-1]
    url = tags.get('href', None)
    if repeat == 1:
        print tags.contents[0]
    repeat -=1
