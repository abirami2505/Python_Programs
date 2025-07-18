#numbers 
n=int(input("Enter the number: "))
for i in range (n,0,-1):
    print(i)

#sting
text=str(input("Enter the string: "))
reverse=" "
for i in text:
    reverse= i+reverse 
print(reverse)