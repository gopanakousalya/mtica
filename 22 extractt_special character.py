def extract_spchar(s):
    spchar=0
    for i in s:
       #print("i=",i)
        if i not in 'bcdefghijklmnopqrstuvwxyz\187246785678356':
            spchar+=1
            #print("i:",i,"temp_vowel:",temp_vowel)
    return spchar
#str1=input("enter the string")
str1=input()
a=extract_spchar(str1)
print(" no of special character in:",str1,"' is",a)
            
