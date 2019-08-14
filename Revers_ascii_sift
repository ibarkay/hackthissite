import requests
import re

#req
headers = {'Referer': 'https://www.hackthissite.org/missions/prog/11/'}
url = 'https://www.hackthissite.org/missions/prog/11/'
cookies = {'PHPSESSID':'YOUR_COOKIE'}
r = requests.get(url,cookies=cookies)
rc =r.content

#RegEx match's for Values
gStringPat = re.findall('[\n\r].*Generated String: \s*([^\<\n\r]*)',str(rc))
shoftPat = re.findall('[\n\r].*Shift: \s*([^\<\n\r]*)',str(rc))

#Algorithem
string = gStringPat[0]
shift  = int(shoftPat[0])
ss = ''

for i in string:
    if i.isdigit():
       ss += i
    else:
        ss+= ','

ss = ss.split(',')
del ss[-1] #deleting last element


result = ''
for i in ss:
    result += chr(int(i)-shift)


#submiting results
rp = requests.post("https://www.hackthissite.org/missions/prog/11/index.php",headers=headers,cookies=cookies, data={'solution':result})
print rp.content

