# def add():
    # a = int(input("Enter number"))
    # b = int(input("Enter Number"))
#     res=a+b
#     print(res)
# if __name__=='__main__':
#     add()

# def add(X,Y):
#     res=X+Y
#     print(res)
# if __name__=='__main__':
#     a = int(input("Enter number"))
#     b = int(input("Enter Number"))
#     add(a,b)

def add(X,Y):
    res=X+Y
    return res
if __name__=='__main__':
    a = int(input("Enter number"))
    b = int(input("Enter Number"))
    res=add(a,b)
    add(a,b)



1)python if-else
:- 
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

if n%2==0:
    if n>=2 and n<=5:
        print("Not Weird")
    elif n>=6 and n<=20:
        print("Weird")
    else:
        print("Not Weird")
else:
    print("Weird")


2)Arithmetic Operators
:-
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    sum = a+b
    print(sum)
    Difference = a-b
    print(Difference)
    product = a*b
    print(product)