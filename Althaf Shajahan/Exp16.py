m=int(input("enter the number of elements"))
print("Enter the elements")
list1=[]
for i in range(0,m):
    n=int(input())
    if(n>100):
      list1.append("over")
    else:
      list1.append(n)
print(list1)
