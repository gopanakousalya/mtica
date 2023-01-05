def reverseString(s):
    ans=[i[::-1] for i in s]
    return ans
inp=input().split()
##print('ayapap tunococ separg ananab')
##print(inp)
print(*reverseString(inp))
