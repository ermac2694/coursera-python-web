import urllib2 as irl
import json

c = 0
url = raw_input('Enter Location: ')
data = irl.urlopen(url).read()
comm = json.loads(data)

print 'Count:', len(comm["comments"])
for item in comm["comments"]:
    c += int(item["count"])
print 'Sum:', c
