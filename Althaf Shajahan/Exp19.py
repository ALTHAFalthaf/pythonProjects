a=int(input("enter the no:of elements:"))
list=[]
for i in range(a):
    n=int(input("Enter the elments:"))
    list.append(n)
print("list items",list)
for i in list:
    if(i%2==0):
        list.remove(i)
print("list after reoving even items:",list)