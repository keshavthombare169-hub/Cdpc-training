#sum of digit
#no=int(input("enter no : "))
#sum=0
#while no>0:
#    rem = no%10
#    sum = sum+rem
#    no=no//10
#print("sum",sum)

# count digit
#no=int(input("enter no : "))
#count=0
#while no>0:
#    no=no//10
#    count=count+1
#print("count",count)

#check no is palindrome
#no=int(input("enter no : "))
#rev=0
#temp=no 
#while no>0:
#    rem = no%10
#    rev = rev*10+rem
#    no=no//10
#if temp==rev:
#    print("palindrome")
#else:
#    print("not palindrome")
 
#check no is arsmstrong    
no=int(input("enter no : "))
sum=0
temp=no 
count=0
while no>0:
    no=no//10
    count=count+1
no=temp
while no>0:
    rem = no%10
    sum=sum+rem**count
    no=no//10
if temp==sum:
    print("arsmstrong")
else:
    print("not arsmstrong")