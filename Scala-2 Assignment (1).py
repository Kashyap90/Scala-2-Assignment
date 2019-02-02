
# coding: utf-8

# In[1]:


# Task 1:

#A Fibonacci series (starting from 1) written in order without any spaces in between, thusproducing a sequence of digits.
# Write a Scala application to find the Nth digit in the sequence.
# Write the function using standard for loop.
# Write the function using recursion.


# In[2]:


# Function using the standard for loop:

def nth_fibonacci_digit_forloop(n):
    prev_minus_two= 1
    prev_minus_one= 1
    if(n==1 or n==2):
        return 1
    else:
        for i in range(3,n+1):
            curr= prev_minus_one+ prev_minus_two
            prev_minus_two= prev_minus_one
            prev_minus_one= curr
        return curr


# In[3]:


n=5
number= nth_fibonacci_digit_forloop(n)
print("{}th fibonacci number is :{} ".format(n,number))


# In[4]:


# Write the function using recursion:

def nth_fibonacci_digit(n):
    if(n==1 or n==2):
        return 1
    else:
        return nth_fibonacci_digit(n-1)+ nth_fibonacci_digit(n-2)


# In[5]:


n=6
number= nth_fibonacci_digit(n)
print("{}th fibonacci number is :{}".format(n,number))


# In[6]:


#Task 2:

#Create a calculator to work with rational numbers.Requirements:

# It should provide capability to add, subtract, divide and multiply rational numbers.
# Create a method to compute GCD (this will come in handy during operations on rational)
#Add option to work with whole numbers which are also rational numbers i.e. (n/1)achieve the above using auxiliary constructors
#enable method overloading to enable each function to work with numbers and rational.


# In[7]:


def calculator(op1,op2,opr):
    value=0.00
    if(opr==1):
        value= op1+ op2
    elif(opr==2):
        value= op1- op2
    elif(opr==3):
        value= op1/ op2
    elif(opr==4):
        value= op1* op2
    elif(opr==5):
        smallest= op2 if(op1>op2) else op1
        while(smallest>=1):
            if(op1% smallest==0 and op2% smallest==0):
                print("GCD of {} and {} is {}".format(op1,op2,smallest))
                break
                smallest=smallest-1
    else:
        print("Invalid choice entered")
        return
    return value   


# In[8]:


print("Enter the choice.\n 1.Addition\n 2.Subtraction\n 3. Division\n 4. MUltiplication\n 5.GCD")
choice= int(input())
number1= int(input("Enter the first number"))
number2= int(input("Enter the second number"))
calculator(number1,number2,choice)


# In[9]:


#Task 3:

#1.Write a simple program to show inheritance in scala.
#2.Write a simple program to show multiple inheritance in scala.


# In[10]:


# 1. Simple program to show inheritance in scala:

class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])
            
class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)

    def findArea(self):
        a, b, c = self.sides
        
        # Calculate the semi-perimeter:
        
        s = (a + b+ c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of trianle is %0.2f' %area)


# In[11]:


t = Triangle()
t.inputSides()
t.dispSides()
t.findArea()


# In[12]:


#2. Simple program to show multiple inheritance in scala.


# In[13]:


class Base(object):
    
    #Constructor
    
    def __init__(self, name):
        self.name = name
        
    # To get name.
    
    def getName(self):
        return self.name
    
# Inherited or Sub class (Note: Person in bracket):

class Child(Base):
    
    #Constructor
    
    def __init__(self, name, age):
        Base.__init__(self, name)
        self.age = age
        
    # To get name:
    
    def getAge(self):
        return self.age
    
        
class GrandChild(Child):
    
    #Constructor:
    
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address
        
    # To get address:
    
    def getAddress(self):
        return self.address
    
g = GrandChild("Alpha1", 25, "Hyderabad")
print(g.getName(), g.getAge(), g.getAddress())


# In[14]:


# Task 4:

#Write a partial function to add three numbers in which one number is constant and twonumbers can be passed as inputs and define 
#another method which can take the partial function as input and squares the result.


# In[15]:


from functools import *

# A normal function:

def add(a, b, c):
    return a+ b+ c

# A partial function:

add_part = partial(add, c = 1)

# Calling partial function:

def square(x=add_part(int(input()), int(input())) ):
    print("The value of the sum is:{}".format(x*x))
    
square()


# In[16]:


# Task 5:

#Write a program to print the prices of 4 courses of Acadgild: Android-12999,Big Data Development-17999,Big Data 
#Development-17999,Spark-19999 using match and add a default condition if the user enters any other course.


# In[17]:


import re

txt = 'Android-12999, Big Data Development-17999, Big Data Development-17999, Spark-19999,'

search= input("Enter the course name")
x = re.findall(r"{}-[0-9]*,".format(search), txt)
for val in x:
    print(x)

