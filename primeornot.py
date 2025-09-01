#method1
num = int(input("Enter the number: "))
for i in range(2,num):
    if num%i==0:
       print("not prime")
       break
else: 
    print("prime")

#method2
num = int(input("Enter the number: "))
is_prime=True
for i in range(2,num):
   if num%i==0:
      is_prime=False
      break
if is_prime:
   print("prime")
else:
   print("not prime")
