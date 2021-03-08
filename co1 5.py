list=[]
for i in range(5):
    x=int(input("enter the nmbr: "))
    if x<100:
        list.append(x)
    else:
        list.append("over")
print(list)