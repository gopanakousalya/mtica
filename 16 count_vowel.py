def count_vowel(s):
    n_vowel=0
    for i in s:
       #print("i=",i)
        if i in 'AEIOUaeiou':
            n_vowel+=1
            #print("i:",i,"temp_vowel:",temp_vowel)
    return n_vowel
#str1=input("enter the string")
str1=input()
a=count_vowel(str1)
print("no of vowels in:",str1,"' is",a)
            
