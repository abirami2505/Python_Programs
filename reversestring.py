#method1 
str=input("Enter the string: ")
reverse=""
for ch in str:
    reverse = ch+ reverse
print(reverse)

#method2
str=input("Enter the string: ")
char_array=list(str)
reverse=""
i=len(char_array)-1
while i>=0:
    reverse +=char_array[i]
    i -=1
print(reverse)
