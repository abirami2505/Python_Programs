num = int(input("Enter the number: "))
reverse=0
original=num
while(num>0):
        digit = num%10
        reverse = reverse*10+digit
        num=num//10
print(reverse)
if(reverse==original):
    print("palindrome")
else:
    print("not palindrome")

