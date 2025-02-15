'''a practice file for iitm bs foundatioal python course'''

"print statement"

print("hello world")
print('hello world')  #single quote or double quotes doesnt matter 
print(12)
print(1.2)

#all three in single print statement 

print('hello world',12,1.2)

'''print must be of right spelling and if opened with a single quotes should be closed with single quotes too'''

#variables 

a=10 #declaration of var
print(a)
a+=1  #increment 

'''getting input from the user '''

print('enter a number')
n=int=input()
print(n)

b=str(input("enter a name"))
print(b)

'''variables and literals concept example  variables change its just a container where value is stored literals values dont change '''

r=float(input("Enter your radius"))
area= 3.14*r*r
#area,r are variable but 3.14 is literal
print(area)

#data type 
c=True
print(type(c))

'''conversion of data type 
float to integer'''

print(int(2.8))

#integer to float 

print(float(2))

#to boolean 

print(bool(2))
print(bool(0)) # only 0 is fals 
print(bool('0'))#as string result true
print(bool(''))#empty string is exception in strings

'''operations and expresions'''

#mixing two strings 
print('spam' + 'eggs')

#adding of list 
print([1,2,3] + [4,5,6])
#elements are repeated 

'''types of operartors'''
#arithmetic operators

#floor division 
print(7//3) #decimal is removed

#modulus operator
print(7%3) #remainder is printed 

#exponential operator
print(2**3) #2*2*2

#relational operators
#greater than,lss than,equal to,not equal to,greater than or equal to,less than or equal to
'''always boolean output'''
print(5>3)
print(5<3)
print(5==3)
print(5!=3)
print(5>=3)

#logical operators
#and,or,not  
print(5>3 and 5<10)
print(5>3 or 5<10)
print(not 5>3)


'''string operations'''
#concatenation  
print('spam' + 'text')

#repetition

print('spam' * 3)

#slicing #acc to indexing 

print('spam'[1]) #index 1
print('spam'[1:3]) #index 1 to 2
print('spam'[:3]) #index 0 to 2
print('spam'[1:]) #index 1 to end
print('spam'[:2]) #index 0 to 1

#comparison in strings 
print("a" < "b")
print("a" > "b")
print("apple" < "mango") #letter by letter comparison
print("apple" < "apricot") #if first letter is same then second letter is compared

#negative indexing
print("python"[-1])  #lasst letter
print("python"[-2])

#lenght of string
print(len("python")) #index=len-1

'''variable naming rules
1.variable name should start with alphabet or underscore
 2.variable name should not start with number
3.variable name should not contain special characters
4.variable name should not contain space
5.variable name should not be a keyword'''
#valid variable name
#_var
#var 

#multiple assignment
x,y=1,2
print(x,y)
x=y=z=10

#swapping
x,y=1,2
x,y=y,x
print(x,y)

#deleting a variable
x=10
print(x)
del x
#print(x) # error if printed 

#short hand operators
count=0
count=count+1
count=count+1
print(count)
#increasing count by 1
count=0
count+=1
count+=1
print(count)
#increasing count same but easy way

#in operator
print("alpha" in "a variable name can only contain alpha-numeric characters and underscores")
print("alpha" in "a variable name must start with a letter or the underscore character") 
#boolen value true if the string is present in the given string

#chaining operators
x=5
print(1<x<10)
print(10<x<20)
print(x<10<x*10<100)
#for output  to be true all the conditions should be true

#escapecaracteres
print("hola\ncomo estas") #blackslash n new line
print("hola\tcomo estas") #blackslash t tab space
print("hola\t\tcomo estas")
#for single quotes
print('hola \'como estas\'')
#for double quotes
print("hola \"como estas\"")

#string methods
#len()
print(len("hola"))

#upper()
print("hi".upper())

#lower()
print("Hello".lower())

#replace()
print("hola".replace("hola","hello"))

#split()
print("hello world ".split(" "))

#count()
print("hay friend ".count("a"))

#isdigit()
print("123".isdigit())

#isalpha()
print("sunny day ".isalpha())
print("123".isalpha())

#isalnum()
print("123".isalnum())
print("123a".isalnum())

#islower()
print("hello".islower())
print("HOLA".isupper())


#startswith()
print("hola como estas".startswith("hola"))

#endswith()
print("hola como estas".endswith("estas"))


 #strip()
print("python coding is fun ".strip(' is fun'))

#lstrip()
print("python coding is fun ".lstrip('python'))

#rstrip()
print("python coding is fun ".rstrip('is fun'))

'''CIPHER SECRET CODE'''
alpha= "abcdefghijklmnopqrstuvwxyz"
s= "sudarshan"
t= ""
i=0
k=1
t=t+((alpha[(((alpha.index(s[i]))+k)%26)]))
t=t+((alpha[(((alpha.index(s[i+1]))+k)%26)]))
t=t+((alpha[(((alpha.index(s[i+2]))+k)%26)]))
t=t+((alpha[(((alpha.index(s[i+3]))+k)%26)]))
t=t+((alpha[(((alpha.index(s[i+4]))+k)%26)]))
t=t+((alpha[(((alpha.index(s[i+5]))+k)%26)]))
t=t+((alpha[(((alpha.index(s[i+6]))+k)%26)]))
t=t+((alpha[(((alpha.index(s[i+7]))+k)%26)]))
print(t)

#move the letter by k units in this case k=1
#we can also use the index of the letter in the string and add k to it
#secrect code is t

'''if statement '''   
#example
print('enter your age ')
age = int(input())
if age >= 18:
  print('you are eligible to vote')
else:
  print(f'you are not eligible to vote, you have {18-age} years to go')

print(f'you are {age}years old') #this print statement is not part of the if statement and gets executed irrespective of the if statement

'''if else elif statement'''
#example 1 
#find whether given number is even or odd
print('enter a number')
num = int(input())
if num % 2 == 0:
  print('even')
else:
  print('odd')
  
  #example 2
#find whether the given number ends with 0 or 5 or any other number
num = int(input("Enter a number: "))
if(num % 5 == 0):
  if(num % 10 == 0):
    print('0')
  else:
    print('other')
    
    #example3 
#grade of students 
grade = int(input("Enter your grade: "))
if grade >= 90:
  print("A")
elif grade >= 80:
  print("B")
elif grade >= 70:
  print("C")
elif grade >= 60:
  print("D")
elif grade >= 50:
  print("E")  
else:
 print("Invalid grade")
  
'''import library'''
#math  libraray

import math
print(math.sqrt(25))
print(math.pow(2,3))
print(math.pi)
print(math.factorial(5))
print(math.log(10))
print(math.log10(10))
print(math.sin(90))  
print(math.cos(90))
print(math.tan(90))
print(math.degrees(90))
print(math.radians(90))
print(math.e)

#random library
import random
a=random.random()  #coin toss simulator
if(a<.5):
  print("Heads")
else:
  print("Tails")
#let us simulate a dice(six faced)
print(random.randrange(1,7))
#let us simulate a dice(six faced)
dice1=(random.randrange(1,7))
dice2=(random.randrange(1,7))
total=dice1+dice2
print("Your pair of dice is:",total)

#different ways to import a library
#caution: if you import a library more than once, then it will be executed only once

#import calendar
import calendar
print(calendar.month(2025,7))
print(calendar.calendar(2025))

#from calendar import *
from calendar import * #import all the content
print(calendar(2025))
print(month(2025,7))

#importing a library
import calendar as c
print(c.month(2025,7))
print(c.calendar(2025))
from calendar import month as m
print(m(2025,7))


'''while loop'''
#syntax while condition:
#   statement
#   statement
#while loop gets repreated until the condition is false

#example 1 
print(f'when did india get its independence (year)?')
year=int(input())
while(year!=1947):
  print("you got this wrong. enter once again.")
  year=int(input())
print("wowww amazing you got it right")


#example 2
#factorial of a number
print("enter a number")
n=int(input())
i=1
answer=1
while(i<=n):
  answer=answer*i
  i=i+1
print(answer)

#example 3
#find the number of digits in the given number
num=abs(int(input("enter a number:")))
digits=1
while(num>9):
  num=num//10
  digits=digits+1
print(digits)

#example 4
#reverse the digits in the given number
num=int(input("enter a number:"))
absnum=abs(num)
if(num>=0):
  rev=num%10
  num=num//10
  while(num>0):
    r=num%10
    num=num//10
    rev=rev*10+r
  print(rev)
else:
  rev=absnum%10
  absnum=absnum//10
  while(absnum>0):
    r=absnum%10
    absnum=absnum//10
    rev=rev*10+r
  print(rev-2*rev)

#example 5
#find whether the entered number is palindrome or not
num=int(input("enter a number:"))
absnum=abs(num)
rev=absnum%10
absnum=absnum//10
while(absnum>0):
  r=absnum%10
  absnum=absnum//10
  rev=rev*10+r
if(num<0):
  rev=rev-2*rev
if(num==rev):
  print("palindrome")
else:
  print("not a palindrome")

'''FOR LOOP'''
 #for loop is used to repeat a set of statements for a fixed number of times
#syntax for i in range(n):
#   statement
#   statement

#example 1 
for i in range(10):
  print("hello india")

#example 2
for i in range(10):
  print(i,"hello india")

#example 3
for i in range(12):
  if(i%2==0):
    print(i,"hello india")
  else:
    print(i,"hi world")

#example 4
#sum of first 10 integers
ans=0
for i in range(10):
  ans=ans+i
print(ans)

#example 5
#multiplication table
for i in range(1,11):
  print("2 x",i,"=",2*i)

#about range function
#range(n)
#range(a,b)
#range(a,b,c)

'''here a is the starting point, b is the ending point and c is the difference between the numbers
only ending point is given then it starts from 0 and goes upto the ending point
only ending point is mandatory and starting point is optional by default the difference between the numbers is 1 and defaut starting point is 0'''

#example 6
for x in range(1,11,2):
  print(x)

#example 7
#decreasing order printing 
for x in range(9,-1,-1):
  print(x)

#example 8 
#for loop without range  for each 
country="india"
for letter in country:
  print(letter)

"formated printing"
#print in same line
#end=''
for x in range(10):
  print(x,end=" ")

#print in different line
#end='\n'  default value of n
for x in range(10):
  print(x)

#sepaarator
#sep=''
d=10
m=5
y=2021
print("today's date is",end=" ")
print(d,m,y,sep='/')

#multiplicaton table using format
num=int(input())
for i in range(1,11):
  print(f'{num} x {i} = {num*i}')
  print('{0} x {1} = {2}'.format(num,i,num*i))
  print('%d x %d = %d'%(num,i,num*i)) # d here is for integer

#format specifier
pi=22/7
print(f'value of pi = {pi}')
print('value of pi = {0}'.format(pi))
print('value of pi = %f'%(pi))

#two decimal places
print(f'value of pi = {pi:.2f}')
print('f value of pi = {0:.2f}'.format(pi))
print('f value of pi = %.2f'%(pi))


#alingment for pattern
print('{0:5d}'.format(1))
print('{0:5d}'.format(11))
print('{0:5d}'.format(111))
print('{0:5d}'.format(1111))
print('{0:5d}'.format(11111))

#for loop examples 

#example 1
#find the factorial of a number
num=int(input())
fact=1
if(num<0):
  print("not defined")
else:
 for i in range(num,1,-1):
   fact=fact*i
   print(fact)

#example 2
#find the number of digits in the given number
num=abs(int(input()))
strnum=str(num)
digits=0
for c in strnum:
  digits=digits+1
print(digits)

'''we should use while loop when we dont know the number of iterations and for loop when we know the number of iterations'''

#nested for loop 

#example 1  
s= 'VIBGYOR'
t='VIBGYOR'
count=0
for i in range(7):
  for j in range(7):
    print(i,j,s[i],s[j])
    count=count+1

print("the total ways in which the two brothers can wear 7 different colours:",count)  

#example 2
#find all prime numbers less than the entered number
num=int(input())
if(num>2):
  print(2,end=' ')
for i in range(3,num):
  flag=False
  for j in range(2,i):
    if(i%j==0):
      flag=False
      break
    else:
      flag=True
  if(flag):
    print(i,end=' ')
    

#example 3
#find the total profit/loss of each trader working in a trading firm. information regarding number of traders and number of transactions is unknown
empID=input('Enter Employee ID:')
while(empID!='-1'):
  trade=int(input('Enter the trade amount:'))
  profit_loss=0
  while(trade!=0):
    profit_loss=profit_loss+trade
    trade=int(input('Enter the trade amount:'))
  print(f'Profit/loss for employee {empID} is {profit_loss}')
  empID=input('\nEnter Employee ID:')
  
  #example 4
#longest word in a string
word = input("Enter a word: ")
maxLen = 0
while(word != "-1"):
  count = 0
  for letter in word:
    count = count + 1
  if(count > maxLen):
    maxLen = count
  word = input("Enter a word: ")

print("The length of the longest word is %s" %maxLen)

#break continue and pass 

email = input()
for c in email:
  if(c == "@"):
    break
  print(c)

email = input()
for c in email:
  if(c == "@"):
    print("")
    continue
  print(c, end = "")

for x in range(11):
  if(x % 3 == 0):
    print(x)
  else:
    pass

'''break and continue are used to alter the normal flow of a loop pass is used to skip the current iteration of a loop to be more specific break is used to exit the loop and continue is used to skip the current iteration of the loop'''

#lists and matrices 
#lists
L= [1,2,3,4,5,6,7,8,9,10]
print(L)
print(L[0]) #first element
print(L[1]) #second element
print(L[2]) # call the 3rd element

L.append(11) # apend adds an element to the end of the list
print(L)

L.remove(10) # remove removes an element from the list
print(L)

L.remove(L[0]) # remove  first  element
print(L)

#in command 
print(2 in L) # true
#whether 2 is in the list L or not 

'''list methods and opeartors'''
#plus operator
L1= [1,2,3]
L2= [4,5,6]
L3= L1+L2
print(L3)

#multiplication operator
L4= L1*3
print(L4)

#indexing
print(L1[0])
print(L1[1])
print(L1[2])

#logical operators ==  equal element and same sequence 
print(L1==L2)
#logical operators != not equal element and same sequence
print(L1!=L2)
#logical operators > greater than
print(L1>L2)
#logical operators < less than 
#comapre the first element of the list
print(L1<L2)

'''mutability'''
#lists are mutable
L2=L1
L1[0]=2
print(L1)
print(L2)

#UNEXPECTED OUTPUT BOTH LISTS ARE CHANGED

'''copying a list'''

#copying a METHODS 
L1= [1,2,3]
L2= list(L1)
L3= L1[:]
L4= L1.copy()
L2[0]=100
L3[1]=200
L4[2]=300
print(L1,L2,L3,L4)

'''IS OPERATOR '''
#HELPS TO CHECK WHETHER THE OBJECTS HAVE SAME  MEMORY OR NOT

#IF THE DATA TYPE IS MUTABLE IT IS CALL BY REFERENCE
#IF THE DATA TYPE IS IMMUTABLE IT IS CALL BY VALUE

#LISTS METHODS 

#append
L= [1,2,3]
L.append(4)
print(L)

#insert
L.insert(2,9)
print(L)

#remove
L.remove(2)
print(L)

#pop
L.pop(0) #deletes the element at the given index
print(L)

#sort
L.sort() #asending order
print(L)

#reverse
L.reverse() 
print(L)

#index
print(L.index(3))

#copy
L.copy()
print(L)


L=[1,1,3,4,5,6,7,8,9,0]
#count
print(L.count(1)) #no of times a element is present 

#extend
L1= [1,2,3]
L2= [4,5,6]
L1.extend(L2)
print(L1)  #extending the list by another list 

#clear
L1.clear() # clears the whole list  empty list is left 
print(L1)

#del
del L1
#print(L1) # error

'''matrix'''
#list of lists
M=[[1,2,3],[4,5,6],[7,8,9]]
print(M)
print(M[0]) #first row
print(M[0][0]) #first element of first row

#list can also take range parameter
p=list(range(10))
print(p)

#set 
#unordered collection of unique elements
S={1,2,3,4,5,6,7,8,9,10}
print(S)
'''searching in set is very fast than in list but set does not allow duplicate elements and takes time to create a set.takes mor memory than list ,cannot name a set as a list(exact elements)'''

import sys
print(sys.getsizeof(S)) #size of set in bytes
print(sys.getsizeof(L)) #Siz of list in bytes

#ADDING ELEMENT TO A SET 

S.add(11)
print(S)

#removing element from a set
S.remove(10)
print(S)

# SET IS MUTABLE BUT EVERY ELEMENT IN A SET MUST BE IMMUTABLE AND HASHABLE(CANNOT BE CHANGED))

#SET METHODS 

A={1,3,5}
B={1,2,3,4,5}

# all normal set of operations can be performed on sets
print(A.issubset(B)) #true
print(A.issuperset(B)) #false

#union of two sets
print(A.union(B))
print(A|B)

#intersection of two sets
print(A.intersection(B))
print(A&B)

#difference of two sets
print(A.difference(B))
print(A-B)
print(B.difference(A))
print(B-A)

#TUPELS
#tuples are immutable used for fixed never changing data
#tuples are created using ()

t= (1,2,3)
print(t,type(t))  #packing
#tuples can be used as keys in dictionaries

#unpacking
x,y,z=t
print(x,y,z)

#single element as tuple 
t=(1)
print(t,type(t)) #int

t=(1,)
print(t,type(t)) #tuple

'''HASHABLE
#hashable means that the object can be changed
#NON HASHAABLE
#lists,dictionaries,sets are non hashable
#value is mutable '''

#tuple can accept list as value 
t=([1,2],['a','b'])
print(t)

#value inside that list can be changed
t[0][0]=10
print(t)

'''FUNCTIONS''' # USER DEFINED FUNCTIONS MODULAR OPERATED PROGRAMMONG 
def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  return x / y

'''TYPES OF ARGUMETNS'''
#PARAMAETERS MEANS THE ARGUMENTS THAT ARE PASSED INTO A FUNCTION
#ARGUMENTS MEANS THE ACTUAL VALUES THAT ARE PASSED INTO A FUNCTION

#POSITIONAL ARGUMENTS
#POSITIONAL ARGUMENTS ARE ARGUMENTS THAT ARE PASSED INTO A FUNCTION IN THEIR POSITION
#POSITIONAL ARGUMENTS ARE REQUIRED 
#EXAMPLE

print(add(5, 10))
print(subtract(5, 10))

#KEYWORD ARGUMENTS
#KEYWORD ARGUMENTS ARE ARGUMENTS THAT ARE PASSED INTO A FUNCTION BY NAME
#KEYWORD ARGUMENTS ARE OPTIONAL

#EXAMPLE

print(add(x = 3, y = 2))

#DEFAULT ARGUMENTS
#DEFAULT ARGUMENTS ARE ARGUMENTS THAT ARE PASSED INTO A FUNCTION WITH A DEFAULT VALUE
#DEFAULT ARGUMENTS ARE OPTIONAL

#EXAMPLE
def add(x, y = 3):
  return x + y

print(add(5))
print(add(5, 2))

'''TYPES OF FUNCTIONS 
INBUILT FUNCTIONS EXAMPLE prin(), input(), len()
USER DEFINED FUNCTIONS EXAMPLE add(), subtract(), multiply(), divide()
STRING METHODS EXAMPLE .upper(), .lower(), .strip(), .split()
USER DEFINED FUNCTIONS EXAMPLE def add(), def subtract(), def multiply(), def divide()'''

'''FUNCTIONAL PROFRAMMING'''
#FUNCTIONAL PROGRAMMING IS A PRACTICE IN PROGRAMMING WHERE PROGRAMMERS SEPARATE THE PROBLEM INTO SMALLER FUNCTIONS

#ITERATOR  
#EXAMPLE
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

basket = iter(fruits)
print(next(basket))
print(next(basket))
print(next(basket))

#reading one line at a time

#GENERATOR
#GENERATOR IS A FUNCTION THAT GENERATES A SEQUENCE OF VALUES
#EXAMPLE

def square(limit):
  x = 0
  while x < limit:
    yield x * x
    yield x * x * x
    x += 1
 
a = square(5)
print(next(a), next(a)) # 0 0
print(next(a), next(a)) # 1 1
print(next(a), next(a)) # 4 8
print(next(a), next(a)) # 9 27
print(next(a), next(a)) # 16 64

'''INLINE STATEMENT'''
#INLINE STATEMENT IS A STATEMENT THAT IS EXECUTED IMMEDIATELY

#EXAMPLE
a = 20
b = 30
'''if a < b:
  small = a
else:
  small = b'''

small = a if a < b else b #ONE LINE IF ELSE STATEMENT
print(small)

#LOOP IN ONE LINE
#EXAMPLE
a = 5
'''while a > 0:
  print(a)
  a -= 1'''
while a > 0: print(a); a -= 1 #ONE LINE WHILE LOOP

#LIST COMPREHENSION
#LIST COMPREHENSION IS A SHORT HAND WAY TO CREATE A LIST

#EXAMPLE
'''NORMAL WAY'''
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)

'''SAME IN ONELINE'''
newlist = [x for x in fruits if "a" in x]
print(newlist)
