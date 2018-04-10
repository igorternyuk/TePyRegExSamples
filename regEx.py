import re

file = open("text.txt")


textToSearch = ""

for line in file:
	textToSearch += line

#print( textToSearch )

patFinder1 = re.compile('C#')
findPat1 = re.search( patFinder1, textToSearch )
if findPat1:
	print( findPat1.group() )
	print( findPat1.start() )
	print( findPat1.end() )
	print( findPat1.span() )

splitFound = patFinder1.split( textToSearch )
if splitFound:
	print( splitFound )

patFinder2 = re.compile('This')
findPat2 = re.findall( patFinder2, textToSearch )
if findPat2:
	for i in findPat2:
		print( i )

patFinder3 = re.compile('C\+{2}')
subFound = patFinder3.sub('C#', textToSearch)
if subFound:
	print( subFound )

