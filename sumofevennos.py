num=int(input("Enter the value: "))
sum=0
for i in range(1,num+1):
    if i%2==0:
        sum+=i
print(sum)

#without modulus
for i in range(2,num+1,2):
    sum+=i
print(sum)

#using math function 
count=num // 2
first=2
last=count*2
sum = count(first+last)//2
print(sum)
