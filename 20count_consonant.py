def count_consonant(s):
    consonant=0
    for i in s:
       #print("i=",i)
        if i in 'bcdefghijklmnopqrstuvwxyz':
            consonant+=1
            #print("i:",i,"temp_vowel:",temp_vowel)
    return consonant
#str1=input("enter the string")
str1=input()
a=count_consonant(str1)
print("consonant in:",str1,"' is",a)
            
