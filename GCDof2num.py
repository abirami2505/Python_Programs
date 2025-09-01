num1=int(input("Number1: "))              #81
num2=int(input("Number2: "))              #153
gcd=1                                    
for i in range(1,num1 and num2):          #division starts from 1 ,18and 153 is range
    
    if(num1%i==0 and num2%i==0):       # the both num should division by the same num which i taken
        gcd=i                           #if gets true then that num should assgin to gcd
print(gcd)

#method2
while(num1!=num2):                        #81!=153
    if (num1>num2):                       #81>153 no 
        num1=num1-num2
    if(num2>num1):                       #153>81 yes so 153-81 =72 num2 is 72
                                         #this happens repeatedly
        num2=num2-num1
print(num1)