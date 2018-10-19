import json
print(json.dumps(True))

import re

print(re.findall('^www\.\s*\.com$','www.baidu.com'))



print(re.findall('^www\..*\.com$','www.baidu.com'))




print('0-9a-f')


s = '(abc)def'
m = re.search("(\(.*\)).*", s)
print(m.group(1))

print(json.loads('null'))

s = "kdla123dk345"
m = re.search("([0-9]+(dk){0,1})[0-9]+", s)
print (m.group(0),m.group(1),m.group(2))


844412

uuid
5fc05447-6f95-4bb5-a833-455d94688ecc


print(json.dumps("{ 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 }"))