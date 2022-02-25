#kavdratlardan list
list=[]
list2=[]
i=0
while i<5:
    a=int(input("Liste eded daxil et:"))
    list.append(a)
    i+=1
for i in list:
    kvadrat=i**2
    if kvadrat>50:
        list2.append(kvadrat)
print(list2)





