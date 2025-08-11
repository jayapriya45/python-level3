print("Takshashila university")
print("ongur,tindivanam")
print("---------------")
print("Student mark list")
m1=int(input("python mark:"))
m2=int(input("DBMS mark:"))
m3=int(input("account mark:"))
total=m1+m2+m3
print("total mark:",total)
average=total/3
print("average mark:",average)
if(m1>=40 and m2>=40 and m3>=40):
    print("pass")
else:
    print("fail")
if(m1>=250):
    print("grade A")
elif(m2>=200):
    print("grade B")
elif(m3>=150):
    print("grade C")
else:
    print("grade D")
