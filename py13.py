print("jayapriya supermarket")
print("nehru street,pondy")
print("bill recipt")
str1=input("enter the item no:")
str2=input("enter the particulars:")
m1=int(input("enter the rate:"))
m2=int(input("enter the quantity:"))
total=m1*m2
print("total amount:",total)
if(total>=10000):
    gst=total*10/100
elif(total>=50000):
    gst=total*5/100
elif(total>30000):
    gst=total*2/100
elif(total>=20000):
    gst=total*2/100
else:
    gst=total*1/100
    print("gst(good service tax):",gst)
amount=total+gst
print("the amount to be paid:",amount)
