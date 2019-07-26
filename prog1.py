import requests
import re

fily = open('wordlist.txt','r') #i manualy got the list 
fily = fily.readlines()

words = []

for i in fily:
    words.append(i.replace('\n','').replace('\r','')) #creat the list of words

cookies = {'cookie':'value'}
r = requests.get('https://www.hackthissite.org/missions/prog/1/',cookies=cookies)
rc = r.content

pattern = re.findall('<li>.{1,10}</li>',rc) #get the scrubled words form the html

scrambles = []

for i in pattern:
    scrambles.append(str(i).replace('<li>','').replace('</li>',''))

unscrumble = '' #the final ans

for i in scrambles:    #compare to sorted strings
    p = ''.join(sorted(i))
    for j in words:
        k = ''.join(sorted(j))
        if k == p :
             unscrumble += str(j)+','

posty = unscrumble[:-1]


headers = {'Referer': 'https://www.hackthissite.org/missions/prog/1/'} #its a have to ..
rp = requests.post("https://www.hackthissite.org/missions/prog/1/index.php",headers=headers,cookies=cookies, data={'solution':posty,'submitbutton':'submit            (remaining time: 30 seconds)'})
print rp.content
