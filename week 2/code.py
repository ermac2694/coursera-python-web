import re
rfile = open("regex_sum_184697.txt")
handle = rfile.read()
n = map(int, re.findall("[0-9]+", handle))
print sum(n)
