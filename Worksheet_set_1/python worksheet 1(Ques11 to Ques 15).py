#!/usr/bin/env python
# coding: utf-8

# Answers of python worksheet question 11 to 15

# In[1]:


#Answer 11
def factorial(n): 
  if n == 1: 
    return 1 
  else: 
    return n * factorial(n-1) 
 
print(factorial(5)) 


# In[2]:


#Answer 12
n= int(input("Enter any number:"))
if(n ==0 or n == 1):
    printf(n,"Number is neither prime nor composite")
elif n>1 :
    for i in range(2,n):
        if(n%i == 0):
            print(n,"is not prime but composite number")
            break
    else:
        print(n,"number is prime but not composite number")
else :
    print("Please enter positive number only ")


# In[3]:


#Answer 13
string=input(("Enter a letter:"))  
if(string==string[::-1]):  
      print("The letter is a palindrome")  
else:  
      print("The letter is not a palindrome") 


# In[5]:


#Answer 14
from math import sqrt
print("Input lengths of shorter triangle sides:")
a = float(input("a: "))
b = float(input("b: "))
c = sqrt(a**2 + b**2)
print("The length of the hypotenuse is:", c )


# In[6]:


#Answer 15
str1 = input ("Enter the string: ")
d = dict()
for c in str1:
    d[c] = d.get(c, 0) + 1
print(d)


# In[ ]:




