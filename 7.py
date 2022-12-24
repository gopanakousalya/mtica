def replace3by5(n):
def replace5by3(m):
    n=str(n)
    m=str(m)
    n=n.replace('3','5')
    m=m.replace('5','3')
    return n
    return m
inp=int(input())
print(replace3by5(inp))
print(replace5by3(inp))
