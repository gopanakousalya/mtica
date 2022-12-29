string='''
practice problems for list com pre hension in python.
'''

wordLst=string.split(' ')
#print(wordLst)
wordLst=[i.strip("\n")for i in wordLst]
print(wordLst)
ans={i:i[::-1]for i in wordLst}
print(ans)
