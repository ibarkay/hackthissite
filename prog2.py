from PIL import Image
import requests

### conect to url and get the img

url = 'https://www.hackthissite.org/missions/prog/2/'
cookies = {'PHPSESSID':'l6h9mkopr5o4kj1vd731cfu593','phpbb3_28pla_u':'1','phpbb3_28pla_k':'','phpbb3_28pla_sid':'b7a6ef76155092637b904da677b283d2'}
r = requests.get(url,cookies=cookies)
rc = r.content

headers = {'Referer': 'https://www.hackthissite.org/missions/prog/2/'}

imgy = 'https://www.hackthissite.org/missions/prog/2/PNG'
ii = requests.get(imgy,cookies=cookies)
open('3.png', 'wb').write(ii.content)


###### Iamge analyzing and ascii ,morse tranlate #####

img = Image.open('3.png').convert("RGB")
width, height = img.size
pixels = img.load()

matches = []

for i in range(width):
    for j in range(height):
        if str(pixels[i,j]) == '(255, 255, 255)': #find the pixeles
            matches.append(int(i)+int(j)*100)
listy = sorted(matches)

Posty = []
for i in range(49):
    if len(Posty) == 0:
        Posty.append(listy[0])
    else:
        Posty.append(listy[1]-listy[0])
        listy.remove(listy[0])
#print Posty
PostyAscii = ''

for i in Posty:
    PostyAscii += chr(i)

#print PostyAscii

##morse translate

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def decrypt(message):

	message += ' '

	decipher = ''
	citext = ''
	for letter in message:

		# checks for space
		if (letter != ' '):

			# counter to keep track of space
			i = 0

			# storing morse code of a single character
			citext += letter

		# in case of space
		else:
			# if i = 1 that indicates a new character
			i += 1

			# if i = 2 that indicates a new word
			if i == 2 :

				# adding space to separate words
				decipher += ' '
			else:

				# accessing the keys using their values (reverse of encryption)
				decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
				.values()).index(citext)]
				citext = ''

	return decipher

result = decrypt(PostyAscii)

result = result[:-1]

#POST

rp = requests.post("https://www.hackthissite.org/missions/prog/2/index.php",headers=headers,cookies=cookies, data={'solution':result})
print rp.content
