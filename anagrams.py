str1=str(input("Enter first String: ")).replace(" ","").lower()
str2=str(input("Enter second String: ")).replace(" ","").lower()
if(len(str1)!=len(str2)):
    print("Not Anagram")
else:
    if sorted(str1)==sorted(str2):
        print("Anagram")
    else:
        print("Not Anagram")