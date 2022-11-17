m=int(input("enter the number of strings"))
print("Enter the strings")
list1=[]
count=0
for i in range(0,m):
  str=input()
  list1.append(str)
print(list1)
for i in list1:
  for j in i:
    if j=='a':
      count=count+1
print(count)