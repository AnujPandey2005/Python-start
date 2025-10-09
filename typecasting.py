#in this video we will learn about type casting
#type casting means converting one data type to another data type
#there are two types of type casting in python
#1. implicit type casting
#2. explicit type casting
#implicit type casting is done by python automatically

x="22"
y=5
print(type(x))
print(type(y))

# z=x+y
# print(z)
# print(type(z))
# this will show error because we are trying to add string and integer
#python will not do implicit type casting here

x=int(x)
z=x+y
print(z)
print(type(z))