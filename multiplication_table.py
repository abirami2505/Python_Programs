table=int(input("Enter the table: "))
for i in range(1,10+1):
    print(table,"*",i,"=",table*i)
    print(f"{table}*{i}={table*i}")


#only the particular multiple table values

table=int(input("Enter the table: "))
num= int(input("Enter the value: "))
for i in range(1,10):
    if i==num:
        print(table,"*",num,"=",table*num)
        print(f"{table}*{num}={table*num}")