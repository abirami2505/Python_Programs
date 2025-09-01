#max of two from user with max()
a=input("Enter the value: ")
b=input("Enter the value: ")

print(max(int(a),int(b)))

#if-else 

a=input("Enter the value: ")
b=input("Enter the value: ")
if a>b:
    print("Greater")
else:
    print("lesser")


#using sort 
num=[a,b]
num.sort()
print(num[-1])