#check if string is anagram or not
def checkAnagram(s1,s2):
    if sorted(s1)==sorted(s2):
        return 'yes'
    else:
        return 'no'
inp=input().split()
print(checkAnagram(inp[0],inp[1]))
