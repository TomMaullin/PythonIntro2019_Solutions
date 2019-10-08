wordsFirstString = firstString.split()
wordsSecondString = secondString.split()
newString = ''

i = 0
while i < len(wordsFirstString):
    
    newString = newString + wordsFirstString[i] + ' ' + wordsSecondString[i] + ' '
    i = i+1
    
print(newString)