##n=int(input())
##if n<0:
##    print('INVALID')
##else:
##    for i in range (n):
##        print('.'*(n-i-1)+'*'*((i*2)+1)+'.'*(n-i-1))









temp1=input().split()
temp2=input().split()
ans=[]
for i,j in zip(temp1,temp2):
    ans.append(int(i)+int(j))
print(*ans)
