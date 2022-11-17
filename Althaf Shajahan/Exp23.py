a=input("Enter the string")
dict1={}
for i in a:
    if i in dict1:
        dict1[i]+=1
        print(dict1)
    else:
        dict1[i]=1
        print(dict1)
print("character frequency")
for k,v in dict1.items():
    print(k,v)
