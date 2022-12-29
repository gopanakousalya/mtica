num1=(input("enter a number:"))
num2=(input("enter a number:"))

try:
    res=int(num1)/int(num2)
except ZeroDivisionError:
    print("handled by kousi")
except ValueError:
    print("handled by madhu")
except Exception as ob:
    print(ob)
else:
    print(num1,'/',num2,'=',res)
finally:
    print('thanks')
print("visit again at python class at mtica")
#123456789
