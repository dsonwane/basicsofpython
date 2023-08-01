# Create first Python project
# Single line comment

"""
multi line comment
using quotes
"""

# variables
x= 5
x="Hello"

print(type(x))
print(x)

X,Y,Z= 10,20,30

print(X,Y,Z)

fruits= ["DIPTI", "NAYNA", "PRIYA"]

A,B,C = fruits

print(A,B,C)

name = "Dipti"

# Functions and reinitialize global member
def demo():
     a=10
     global name

     name ="Nayna"
     print("value of a", a)

demo()

def add(a,b):
  return a+b

res = add(10,20)

print("res of add = ", res)

print(x)

print("global name ", name)


if 5>2:
  print("Five is greater than two")

#Operator

c, d = 20,30

print("add c+d = ",c+d)
print("sub d-c = ",d-c)
print("mult c*d =", c*d)
print("div d/c = ", d/c)


