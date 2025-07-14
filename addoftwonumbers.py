#from the user 
num1=input("Enter the value: ")
num2=input("Enter the value: ")

sum=int(num1)+int(num2)

print(sum)

#add using fun
def add(a,b):
    return(a+b)
a=input("Enter the value: ")
b=input("Enter the value: ")

res= add(int(a),int(b))
print(res)

#builtin opertor 
import operator
print(operator.add(10,3))

