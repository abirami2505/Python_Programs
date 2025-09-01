num = int(input("Enter the number: "))     #125
length=len(str(num))                       #3
temp=num                                   #temp=125
sum=0
while(temp>0):                             #125>0       #12>0            #1>0
    digit=temp%10                          #125%10=5    #12%10=2         #1%10=1
    sum +=digit**length                    # 5**3=125   #2**3=8+125=133   #1**3=1+133=134
    temp=temp//10                          #125//10=12  #12//10=1         #1//10=0
print(sum)
if(sum==num):                             #134!=125
    print("Armstrong")
else:
    print("not armstrong")