
'''a = int(input("enter : "))
b = str(input("enter : "))
c = bool(input("enter : "))
d = float(input("enter : "))
print (type(a), a)
print (type(b), b)
print (type(c), c)
print (type(d), d)

num = (int(input("enter a number : ")))  # input function    
w = num                    # if else statement 
if num > 0:
     print ("positive")
elif num < 0:
     print ("negative")
else:
     print ("zero")


     file = open("imp_backup_nuclear_codes_.txt", "r")
for line in file:
     line.strip() 





     # arrays 
arr = [1, 2, 3, 4, 5]
tuples = (1, 2, 3, 4, 5)
lists = [1, 2, 3, 4, 5]
sets = {1, 2, 3, 4, 5}
dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
for i in range(len(arr)):
     print (arr[i])
for x in range(len(tuples)):
     print (tuples[x])

for x in range (1,10,10):  # for loop 
     print (x)

lists.append("Lion")
lists.append("Tiger")
lists.append("Bear")
print (lists)
'''

# dont go up 
'''
def greet(name):
    print ("hello", name)


greet("lucky")
greet("om")
greet("ansh")

def add(a,b):
     return a + b
def subtract(a,b):
     return a - b 
def divide(a,b):
     return a / b 
def multiply(a,b): 
     return a * b 

print (add(5, 10)) 
print (subtract(10, 5)) 
print (divide(10, 2)) 
print (multiply(5, 2)) 
 



def square(x):
    return x * x

result = square(5)

print(result)




def feet_to_cm(feet):
     return feet * 30.48                                                  
cm = feet_to_cm(float(input("enter height in feet: ")))
print(cm)



def cm_to_inch(cm):
     return cm / 30.48
inch = cm_to_inch(float(input("enter cm : ")))
print(inch)

def theory_of_relativity(mass):
     return mass * 299792458 ** 2

energy = theory_of_relativity(float(input("enter mass : ")))
print(energy)



import math


nums = [float(x) for x in input("enter the numbers separated by space: ").split()]

print ("sum", sum(nums))
print ("max", max(nums))
print ("min", min(nums))

'''







class Student:
    def __init__(self, name):
        self.name = name

student1 = Student("Alice")
student2 = Student("Bob")


print("Student 1:", student1.name)
print("Student 2:", student2.name)