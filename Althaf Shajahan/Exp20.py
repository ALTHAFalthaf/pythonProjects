a=int(input("Enter the number of elements:"))
n1, n2= 0, 1
print("fibonacci series:",n1,n2)
for i in range(2,a):
    b=n1+n2
    n1=n2
    n2=b
    print(b)

