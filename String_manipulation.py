import requests
import re

#req
headers = {'Referer': 'https://www.hackthissite.org/missions/prog/12/'}
url = 'https://www.hackthissite.org/missions/prog/12/'
cookies = {'PHPSESSID':'YOUR_COOKIE_HERE','phpbb3_28pla_u':'1','phpbb3_28pla_k':'','phpbb3_28pla_sid':'b7a6ef76155092637b904da677b283d2'}
r = requests.get(url,cookies=cookies)
rc =r.content

#Get value's by Regex
a = re.findall('[\n\r].*value="\s*([^"\n\r]*)',str(rc))
a = a[0]

#Algorithem
nOfstring = []
for i in str(a):
    if i.isdigit():
        if int(i) != 0 and int(i) != 1:
            nOfstring.append(i)


#check if prime
def ifPrime(num):
    if num > 1:

        # Iterate from 2 to n / 2
        for i in range(2, num):

            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return 0
        else:
            return 1

    else:
        return 0

#prims and nots
primeis = []
constys = []
for i in nOfstring:
    if ifPrime(int(i)) == 0:
        constys.append(int(i))
    else:
        primeis.append(int(i))


#math
sPrims = sum(primeis)
sConstys = sum(constys)
multip =  sPrims * sConstys

#non Digits part
nonDigits = ''
for i in str(a):
    if i.isdigit():
        pass
    else:
        nonDigits += i
nonDigits = nonDigits[0:25] #only fist 25


result = ''
for i in nonDigits:
    result += chr(ord(i)+1) #up by 1 ASCII

result += str(multip) # add the multipy of prmes and const (math) to the result


#finally SUBMIT result --- note that submitbutton data is a must
rp = requests.post("https://www.hackthissite.org/missions/prog/12/index.php",headers=headers,cookies=cookies, data={'solution':result,'submitbutton':'Submit (remaining time: 5 seconds)'})
print rp.content



