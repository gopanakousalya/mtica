def remove_duplicate(s):
    str2=''
    for i in s:
       #print("i=",i)
        if i not in str2:
            str2+=i
            print(str2)
            #print("i:",i,"temp_vowel:",temp_vowel)
    return str2
#str1=input("enter the string")
str1=input("enter your text:")
print("without duplicate:",remove_duplicate(str1))
            
