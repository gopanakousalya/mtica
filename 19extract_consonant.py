def extract_consonant(s):
    consonant=''
    for i in s:
       #print("i=",i)
        if i in 'bcdefghijklmnopqrstuvwxyz':
            consonant+=i
            #print("i:",i,"temp_vowel:",temp_vowel)
    return consonant
#str1=input("enter the string")
str1=input()
a=extract_consonant(str1)
print("consonant in:",str1,"' is",a)
            
