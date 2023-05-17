Answers of python worksheet question 11 to 15


```python
#Answer 11
def factorial(n): 
  if n == 1: 
    return 1 
  else: 
    return n * factorial(n-1) 
 
print(factorial(5)) 
```

    120
    


```python
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
```

    Enter any number:12
    12 is not prime but composite number
    


```python
#Answer 13
string=input(("Enter a letter:"))  
if(string==string[::-1]):  
      print("The letter is a palindrome")  
else:  
      print("The letter is not a palindrome") 
```

    Enter a letter:hello sir
    The letter is not a palindrome
    


```python
#Answer 14
from math import sqrt
print("Input lengths of shorter triangle sides:")
a = float(input("a: "))
b = float(input("b: "))
c = sqrt(a**2 + b**2)
print("The length of the hypotenuse is:", c )
```

    Input lengths of shorter triangle sides:
    a: 12
    b: 16
    The length of the hypotenuse is: 20.0
    


```python
#Answer 15
str1 = input ("Enter the string: ")
d = dict()
for c in str1:
    d[c] = d.get(c, 0) + 1
print(d)
```

    Enter the string: Hello
    {'H': 1, 'e': 1, 'l': 2, 'o': 1}
    


```python

```
