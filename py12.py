print("government of tamilnadu")
print("electricity board")
print("----------------")
print("bill recipt")
print("------------------")
str1=input("enter the eb number:")
str2=input("enter the name:")
unit1=int(input("enter the previous unit:"))
unit2=int(input("enter the current unit:"))
unit=unit2-unit1
print("unit consumed:",unit)
if(unit>=1000):
    amount=unit*10
    print("amount to be paid:",amount)
elif(unit>=500):
    amount=unit*5
    print("amount to be paid:",amount)
elif(unit>=100):
    amount=unit*2
    print("amount to be paid:",amount)
else:
    print("amount to be paid:",amount)
          
          
           
