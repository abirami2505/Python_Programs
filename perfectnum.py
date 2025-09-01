num =int(input ("Enter the number: "))
i=1
sum=0
while(i<=num//2):
    if(num%i==0):
      sum +=i
      i +=1
print(sum)
if(num==sum):
   print("Perfect number")
else:
   print("Not Perfect number")