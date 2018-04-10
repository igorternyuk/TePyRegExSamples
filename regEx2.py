import re

textAboutLinux = open("linux.txt")

textToSearch = ""

for line in textAboutLinux:
	textToSearch += line

patFinder1 = re.compile( '[a-z]+\s', re.IGNORECASE )
findPat1 = re.findall( patFinder1, textToSearch )

if findPat1:
	for i in findPat1:
		print( i )

digitFinder = re.compile('\d+')
findDigit = re.findall( digitFinder, textToSearch )

if findDigit:
	for i in findDigit:
		print( i ) 

print("***Strange thing***")
#StrangeThing:12B + -G 
patFinder2 = re.compile('[a-zA-z]+:\d+\D\s\S.\W\w')
findStrangeThing = re.findall( patFinder2, textToSearch )
if findStrangeThing:
	for i in findStrangeThing:
		print(i)

patFinder3 = re.compile( '[Сс]истем[а-я]{0,2}[\,|\.|\s]' )
findPat3 = re.findall( patFinder3, textToSearch )
if findPat3:
	for i in findPat3:
		print(i)

patFinder4 = re.compile( '[A-Z]+\d+[\s|\.\,]', re.IGNORECASE )
findPat4 = re.findall( patFinder4, textToSearch )

if findPat4:
	for i in findPat4:
		print( i )