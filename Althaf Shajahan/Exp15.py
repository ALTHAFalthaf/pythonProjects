list1=[1,2,3,4,5]
list2=[7,8,9]
if len(list1)==len(list2):
    print("length of the list are same")
else:
    print("length of the list are different")
a=sum(list1)
print(a)
b=sum(list2)
print(b)
if a==b:
    print("sum of both list are same")
else:
    print("sum of both list are different")

c=set(list1)&set(list2)
if c:
    print("both have common elements")
else:
    print("both does not have common elements")