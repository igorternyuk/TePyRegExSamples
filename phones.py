import re

file = open('fonos.txt')

textToSearch = ""

for line in file:
	textToSearch += line

phoneFinder = re.compile('(\+?[0-9]{1,3}-?[0-9]{2,3}-?[0-9]{2,3}-?[0-9]{2,3}-?[0-9]{2,3})|(\+?\(?[0-9]{1,3}\)?-?\(?[0-9]{2,3}\)?-?\(?[0-9]{2,3}\)?-?\(?[0-9]{2,3}\)?-?\(?[0-9]{2,3}\)?)')
findPhone = re.findall( phoneFinder, textToSearch )

if findPhone:
	for phones in findPhone:
		for p in phones:
			if p != '':
				print( p )

nameFinder = re.compile('(Свет[лана|а|ик|уля|очка|ка|усик]{1,4})|(Лан[а|очка|уся]{1,4})')
findName = re.findall( nameFinder, textToSearch )

if findName:
	for names in findName:
		for n in names:
			if n != '':
				print( n )