import urllib2 as irl
import xml.etree.ElementTree as et

c = 0
url = raw_input('Enter Location: ')
data = irl.urlopen(url).read()
tree = et.fromstring(data)
comm = tree.findall('comments/comment')

print 'Count:', len(comm)
for item in comm:
    c += int(item.find('count').text)
print 'Sum:', c
