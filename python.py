# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 13:41:37 2023

@author: Arslan
"""

a=31
print(type(a))

b="31"
print(type(b))

name="HARRY"
print(len(name))

L1=[1,2,3,4,"harry"]
L1[1]=9
print(L1[4])

d=[5,6,9,33,65]
print(d[0:2])

a={"key":"value","harry":"code","marks":"100","list":[1,2,3]}
print(a["key"])
    
a={"key":"value","harry":"code","marks":"100","list":[1,2,3]}
print(a["list"])

a={"name":"ali","from":"pakistan","marks":[98,92,99]}
print(a.items())

a={"name":"ali","from":"pakistan","marks":[98,92,99]}
print(a.keys())

a={"name":"ali","from":"pakistan","marks":[98,92,99]}
print(a.get("name"))

a=[1,2,3]
b=[4,5,6]
print(a+b)

a=22
if(a>9):
    print("greater")
else:
    print("lesser");
    
a=list(range(10))
b=a
b[0]=100
print(a)

for i in range(0,7):
    print(i)

for i in range(0,80):
    print(i)
    if i==3:
        break
    
    for i in range(4):
        print("printing")
        if i==2:
            continue
        print(i)
        
l=[1,7,8]
for item in l:
    print(item)
   
gr="hello"+name
print(gr)

