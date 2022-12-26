def extract_digit(s):
    n_digit=0
    for i in s:
       #print("i=",i)
        if i in '0123456789':
            n_digit+=1
            #print("i:",i,"temp_vowel:",temp_vowel)
    return n_digit
#str1=input("enter the string")
str1=input()
a=extract_digit(str1)
print("no of digits in:",str1,"' is",a)
            
