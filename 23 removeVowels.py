def removeVowels(s):
    temp=''
    for i in s:
       #print("i=",i)
        if i not in 'AEIOUaeiou':
            temp+=i
            #print("i:",i,"temp_vowel:",temp_vowel)
    return temp
#str1=input("enter the string")
str1=input()
a=removeVowels(str1)
print("string",str1,"without vowel is",a)
            
