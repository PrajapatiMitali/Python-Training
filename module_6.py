# Module 6) Python Fundamentals

# ==============================================
# 1. Introduction to Python
# ==============================================

#  Write a Python program that prints "Hello, World!".

print("Hello World")

# PS C:\Users\Dell> python
# Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> print("hello World")
# hello World


# ==============================================
# 2. Programming Style
# ==============================================

#Write a Python program that demonstrates the correct use of indentation, comments,
# and variablesfollowing PEP 8 guidelines.

#Single line comment
def my_world():
    ''' Here is a demo isllustartion single ,
        multi line comments , this iwll also considered a doc string,
        in prior if i print doc string this will print
    '''

    """ This is my world function and also a doc string"""
    print("I am in my world function")  # Identation

print(my_world.__doc__)
my_world()



# ==============================================
#   3. Core Python Concepts
# ==============================================  

# Memory allocation of varibales
x = 10
y = 10
print(id(x))
print(id(y))

#the memory allocation of x and y will be same
print(x is y)

a = 84657465848584365746574757436574657647564
b= 84657465848584365746574757436574657647564
print(a is b)

c = d = 846584657465745
print(c is d)

my_list = [1,2,3]
my_list_1 = [1,2,3]
print(my_list is my_list_1)

#==============================================================
# Python variables
#==============================================================
# Variables are containers for storing data values
# Variables are created when you assign a value to it
a = "apple"  # string can be declared in double and single quotes
# OR a = 'apple'
b = "banana"

print(a)
print(b)

x ,y, z = 10 , "mango", 7.9
print(x)
print(y)
print(z)

my_var_1 =my_var_2=my_var_3 = "honda"

print(my_var_1)
print(my_var_2)
print(my_var_3)


# Output Varibales
# print() is often used as output variables

#Input Variables
#input() is used as input variables

x = "apple"
y = "mango"

print(x+y)
print("I love " + x )

a = 10
b = 20
print(a+b)

a = "10"
b = 20
#print(a+b) #TypeError: can only concatenate str (not "int") to str

print(int(a)+b)

# this is known as type conversation
#Scope of varibales

#varibales thatare created out side the function are knwon as global varibales
#we can also define the global varibales using global keyword and can define anywhere in the program

x = "hello"
def my_fun_one():
    x= "world"
    print("in the function", x)

print("x=",x)# x= hello
my_fun_one() #in the function world
print("x=",x)

x = "hello"
def my_fun_one():
    global x
    x= "world"
    print("in the function", x)

print("x before global declaration=",x) #hello
my_fun_one() #in the function world
print("x=",x)# x= world

#===================================================================
# Understanding data types: integers, floats,strings, lists, tuples, dictionaries,sets.
#============================================================================

#String 

#String is a seqeunce of unicode characters
#String is a group of characters
#String are immutabe
#String are indexable

my_string = "Hello World"
print(len(my_string))
print(my_string[1])

#It is indexable, the indexing starts from the 0
#Python also allow negative indexing
#It also allow the space to be count in the string
print(my_string[-1])

#my_stirng([start:stop:step])
#it will give start:stop-1:step 
#String slicing
print(my_string[0:2])
print("---------",my_string[:5])
print("---------",my_string[5:])
print("---------",my_string[-5:-2])


#Reverse a string
print(my_string[::-1])
  
#if nothing is written it will consider it as omiited
print(my_string[:-1])

for i in "apple":
    print(i)
    print(i,end="")
#Check in strings

a = "This is python"
print("is" in a)
print("th" in a)
print("on" in a)
print("is " in a)
print("" in a)

print(a.upper())
print(a.lower())
#strip removes whitespaces form the begginning and the end
b = "   helloooo world  hello apple "
print(b.strip())
print(b.replace("hello","apple"))
print(b.replace("l","b"))
print("****************************************************")
print(b.startswith("a"))
print(b.rpartition("o"))
print(b.isnumeric())
print("-------",b.rfind("hello")) # return the index where this data is find first
#Python String Operations
c= "Good Morning, Everyone"
#split
print(c.split(","))  # Split it form the ,
a = ["apple","mango"]
cid = ' '.join(a)
print("-----------------CID---------------",cid)
#Sting Format
print('Hello my name is {}'.format("apple"))
print('hello my name is {} and {}'.format('apple','mango'))
print('hello my name is {1} and {0}'.format('apple','mango'))
print('hello my name is {0} and {0}'.format('apple','mango','banana'))

print(f'My name is {c}')

price = 974
print(f'The price of the mango is {price}')
print(f'The price of the mango is {price:.2f}') #The price of the mango is 974.00
print(f'The price of the mango is {10*40}, {746+7467}')


#Repetition in string
s1 = "HEllo"
print(s1*3)

#Escape characters
print("hello my nameis 'hello'")
print("my name is \"hello\" ok")
print("hello \n all")  # New line
print("Hello \\ is ok") #It will give\ instead of \\
print("he \r llo all")  # carriage return  llo all


#String Comparison

a = "hello"
b = "World"
c = "World"
print(a==b)
print(b==c)

#=============================================================
#List
#=============================================================
#List is a orderd sequence of items
#List are indexable,mutable,allow duplicates
#can store data of any data type
#allow negative indexing

#declaration or empty list
my_list = list()
my_list_1 = []

my_lst = [1,2,3,4,"apple",["hello","world"],9,19,{'ok':"apple","ok_1":"mango"}]
print(my_lst)
print(len(my_lst))
print(my_lst[8])
print(my_lst[8]['ok'])
print(my_lst[5])
print(my_lst[5][1])

#Add elements to python list
my_list.append(7)
my_list.append("apple")
print(my_list)

my_data = [1,2,"10","mango"]
for i in my_data:
    my_list.append(i)

print(my_list)

#Add elemenets at specific index

my_list.insert(4,"banana")
print(my_list)

my_list[4] = "Pine Apple"
print(my_list)

#extend and append

a= [1,2,3]
b= ["x","y","z"]

a.extend(b)
print(a)

a.append(b)
print(a)

#Remove items from the list
a.remove(2) # 2 is item not index
print(a)

#Get the index of the specified value
print(a.index("x"))

#using the index
a=[1,2,"n","a","apple","n","mango","pipne apple"]
print(a.index("n"))
print(a.index("n",5))
print(a.count("n"))
print(a.count(" "))
print(a.pop(2))  #remove the particular index
print(a.remove("apple")) # remove the element
print(a.pop())
print(a) 

my_data = a.pop(3)
print(my_data)
print(a)
a.append("World")
a.insert(2,"helo")
print(a)

#Reverse the python list
print(a[::-1])
a.reverse()
print(a)

print(reversed(a))
for i in reversed(a):
    print(i)

my_list_data = [1,2,9,6,83,6,23]
my_list_data.sort()
print(my_list_data)

my_list_data_1 = ["apple","mango","cherry","berry","banana"]
my_list_data_1.sort()
print(my_list_data_1)

my_list_data_2 = my_list_data_1.copy()
print(my_list_data_2)
my_list_data_2.append("data")
print(my_list_data_2)
print(my_list_data_1)

a = [1,2,3]
b = a
print(a)
a.append("me")
print(b)

b.clear()
print(b)

del b
# print(b) it is dleeted from the memory


#============================================================
#Tuple
#============================================================
#Tuple is orders sequence list
#tuples are immutable
#once tuple is created it can not be modified
#tuples are used to store protected data as it can not be modified
#tuples are faster than list

t = (1,2,3)
print(type(t))  # tuple

t= (1)
print(type(t))  #int

t = (1,)
print(type(t))  #tuple

t = (1,2,3,[1,2,3])
print(t[0])
print(t[3])
print(t[3][1])
t[3][1] = "apple"
print(t)

# we can perform del, count ,indexing ,len on tuples
t = (1,2,3,0,76,9)
new_t = sorted(t)
print(new_t)

#================================================================
#Set
#=================================================================

#set does nt allow duplicated
#set are unorderd collection of items
#as set are unordered collection of data,it does not allow indexing
# set can be usedto perform athematical operations like union ,intersection etc

my_set = set()
print(type(my_set))

my_set_1 = {1,2,3,3}
print(my_set_1)

#Convert list into set
s = set([1,2,2,3,4])
print(s)

#we can add data in set like

s.update({"apple","mango"})
print(s)

s.remove("apple")
print(s)

# s.remove("data")
# print(s) it will give error as it set doed not contains "data" so we can use discard

s.discard("data") # if data is there it will remove it or else does not throw error
print(s)

s.pop() #remove any data from the set
print(s)

s.clear() 

#Mathematical operations on the set
s1= {1,2,3,4}
s2 ={6,7,8,1,2}

print(s1.union(s2))  # give all the values
print(s1.intersection(s2)) #give the common values from s1 and s2
s3 = s1-s2 # differnce  {3, 4}
print(s3)

s3 = s1 ^ s2 #symmetic diffence
print(s3) #{3, 4, 6, 7, 8} 

print(s1.issubset(s2))

#=========================================================
#Dictionary
#========================================================
#Dictionary is the most powerful and useful data type in python
#It is an unorderd collection of items 
#In dictionary data are stored in key value pair

#declare the empty dictonary
my_dict = {}
my_dict_1 = dict()

my_dict['1'] ="apple"
print(my_dict)

my_dict['2'] ="mango"
print(my_dict)

my_dict['2'] ="pine"
print(my_dict)

#1,2 re key and apple , mango ,pine are values
#Create dictionary form list of tuples
my_dict_1 = dict([(1,'abc'),(2,'cde'),(3,'xyz')])
print(my_dict_1)

#Accessing the value from the dictionary
print(my_dict_1[1])
print(my_dict_1.get(7,None))

#Remove the items from the dictonary
print(my_dict_1.pop(1))
print(my_dict_1)

#Remove an aribiary item
print(my_dict_1.popitem())
print(my_dict_1)

#delete 
# del my_dict_1

#clear
# my_dict_1.clear()

my_dict = {1:1,2:4,3:9,4:16,5:25}
print(my_dict)
print(my_dict.keys()) #dict_keys([1, 2, 3, 4, 5])
print(my_dict.values()) #dict_values([1, 4, 9, 16, 25])
print(my_dict.items()) #dict_items([(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)])

for key,value in my_dict.items():
    print("key is =" ,key, "and" , "value is =", value)

for key in my_dict.keys():
    print(key,end=" ")

for values in my_dict.values():
    print(values)

for k,v in my_dict.items():
    if k>2:
        print({k:v})

my_data = {k:v for k,v in my_dict.items() if k>2}
print(my_data)

#==================================================================================
#Python operators: arithmetic, comparison, logical, bitwise.
#=========================================================================
# Arithematic = +,-,%,\,\\, % , **
# Assigment = += , -=, %= ,/=
# Comparison = ==, >,< ,>=,<= , ! , !=
# logical =  and, or ,not
# Bitwise = &, | ,>>,<<
# Special =is , is not, in,not in

# Practical Example 1: How does the Python code structure work?
# Practical Example 2: How to create variables in Python?
my_var = "apple"
a = 10
# Practical Example 3: How to take user input using the input() function.
# num_1 = int(input("Enter the number 1 : "))
# num_2 = int(input("Enter the number 2 : "))
# num_3 = num_1 + num_2
# print("The addition of {num_1} and {num_2} is ", num_3)

# numbers = int(input("Enter the numbers you want to add: "))
# t = 1
# sum = 0
# while t <= numbers:
#     num = int(input("Enter the numbers: "))
#     t+=1
#     sum+=num

# print(f"The addition of given numbers is {sum}")

# Practical Example 4: How to check the type of a variable dynamically using type().
data = "apple"
print(f"The type of {data} is {type(data)}")

data = 1
print(f"The type of {data} is {type(data)}")

num1 = 3
num2 = 5.4

print(type(num1))
print(type(num2))

num3 = num1+num2
print(type(num3))


#=====================================================================================
#4. Conditional Statements
#=======================================================================================

#: Write a Python program to find greater and less than a number using if else
# num_1 = int(input("Enter number 1: "))
# num_2 = int(input("Enter number 2: "))

# if num_1 > num_2:
#     print(f"Number 1 :  {num_1} is greater")
# else:
#     print(f"Number 2 : {num_2} is greater")

# Practical Example 6: Write a Python program to check if a number is prime using if_else.
# num = int(input("Enter the number : "))
# if num > 1:
#     for i in range(2,num):
#         if (num % i) == 0:
#             print(f"Number : {num} is not prime")
#             break
#         else:
#             print(f"Number : {num} is prime")
#             break
# else:
#     print(f"Number : {num} is not prime")
 
# Practical Example 7: Write a Python program to calculate grades based on percentage using if else ladder

# percentage = int(input("Enter the percentage: "))
    
# if percentage < 0 or percentage >100:
#     print("Enter proper percentage:")
#     exit()
# if percentage > 90 and percentage <= 100:
#     print("You score A+ grade")
# elif percentage > 80 and percentage <=90:
#     print("You score A grade")
# elif percentage >70 and percentage <=80:
#     print("You score B+ grade")
# elif percentage >60 and percentage <=70:
#     print("You score B grade")
# elif percentage >50 and percentage <=60:
#     print("You score C+ grade")
# elif percentage >40 and percentage <=50:
#     print("You score C grade")
# else:
#     print("You failed in exam")

# Practical Example 8: Write a Python program to check if a person is eligible to donate blood using a nested if.
# age = int(input("Enter the age of the person: "))
# weight = int(input("Enter the weight of the person: "))
# disease = str(input("Is there any diease ? , Enter yes  or no : "))

# if disease in ["yes","Yes"]:
#     disease_in_person = True
# elif disease in ["no","No"]:
#     disease_in_person = False
# else:
#     print("Please Enter proper yes or no")
#     exit()

# if disease_in_person:
#     print("You are not able to donate blood as of disease")
# else:
#     if age < 18:
#         print("You are not able to donate blood, As you are underaged")
#     else:
#         if weight < 40:
#             print("You are not able to donate blood, as your weight is less")
#         else:
#             print("You are eligible for donating blood")

#===========================================================================
#5. Looping (For, While)
#============================================================================
for i in range(5):
    print(i,end=" ")

print("\n====================================")

for i in range(1,10):
    print(i,end=" ")

print("\n====================================")
for j in range (1,20,2):
    print(j,end=" ")


print("\n====================================")

my_lst = [1,2,3,4,5]
for i in my_lst:
    print(i,end=" ")

print("\n====================================")

my_lst = [1,2,3,4,5]
for i in my_lst:
    print(i,end=" ")
else:
    print("Ended")
print("\n====================================")

data = "Hello how are you"
for i in data:
    print(i,end=" ")

print("\n====================================")

#Find the factorial of the given number
# num = int(input("Enter the number: "))
# fact = 1
# for i in range(1,num+1):
#     fact*=i
# print("factorial of given number is :", fact)

# While loops
# num = int(input("Enter the number: "))
# t = 1
# while t <=5:
#     print("i am in loop:")
#     t+=1

# while True:
#     age = int(input("Enter your age: "))
#     if age > 18:
#         print("You are able to vote")
#     else:
#         print("not able to vote")


#Break and continue:

for i in range(10):
    if i == 5:
        break
    else:
        print(i)

print("\n====================================")

for i in range(10):
    if i == 6:
        continue
    else:
        print(i)


tup = (1,2,"apple")
for i in tup:
    if i == 2:
        print("yes")
    else:
        print("No")

# Practical Example 1: Write a Python program to print each fruit in a list using a simple for loop. List1 = ['apple', 'banana', 'mango']
List1 = ['apple', 'banana', 'mango']
for i in List1:
    print(i)

# Practical Example 2: Write a Python program to find the length of each string in List1.

List1 = ['apple', 'banana', 'mango']
for i in List1:
    print(i," ", len(i))

for i in List1:
    count = 0
    for j in i:
        count +=1
    print(f"length of {i} is {count}")

# Practical Example 3: Write a Python program to find a specific string in the list using a simple for loop and if condition.
List1 = ['apple', 'banana', 'mango']
for i in List1:
    if i == "banana":
        print("Got the word")

# Practical Example: 1) Write a Python program to skip 'banana' in a list using the continue statement. List1 = ['apple', 'banana', 'mango']

List1 = ['apple', 'banana', 'mango']
for i in List1:
    if i == "banana":
        continue
    else:
        print(i)
# Practical Example: 2) Write a Python program to stop the loop once 'banana' is found using the break statement.

List1 = ['apple', 'banana', 'mango']
for i in List1:
    if i == "banana":
        break
    else:
        print(i)
# List1 = ['apple', 'banana', 'mango','cherry','data']
# word = str(input("Enter the word to be find in list: "))
# for i in List1:
#     if i == word:
#         print("Got the word")
#         break

# Practical Example 4: Print this pattern using nested for loop:
for i in range(1,6):
    print("* "*i)

#===========================================================
#6. Generators and Iterators
#===========================================================

#Iterators
# iter for any value (list,tuple, etc)
#iter() fucntion is used to iter over the object
#next() function is used to call the next elemenet in the iterable object
data = iter(['Apple','mango','banana','cherry'])
print(next(data))
print(next(data))
print(next(data))
print(next(data))

#Genarators
#another way of using iterators is yield
def do_sqaure(num):
    for i in range(1,num+1):
        yield i*i 

a = do_sqaure(5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print("\n==============================================================")
# Write a generator function that generates the first 10 even numbers.
def generate_even_no():
    num = 2
    count = 0
    while count <=10:
        num+=2
        count+=1
        yield num
       

a = generate_even_no()
print(a)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

for i in a:
    print(i)

# Write a Python program that uses a custom iterator to iterate over a list of integers.


#=============================================================
#7. Functions and Methods
#====================================================================
# Practical Example: 1) Write a Python program to print "Hello" using a string.
print("Hello World")

# Practical Example: 2) Write a Python program to allocate a string to a variable and print it.
my_str = "Hello World"
print("my str: ",my_str)

# Practical Example: 3) Write a Python program to print a string using triple quotes.
my_str = """My String """
print(my_str)

#Practical Example: 4) Write a Python program to access the first character of a string using index value.
my_str = "Good Morning Everyone"
print(my_str[0])

#Practical Example: 5) Write a Python program to access the string from the second position onwards using slicing.
print(my_str[1:])

# Practical Example: 6) Write a Python program to access a string up to the fifth character.
print(my_str[0:5])

#Practical Example: 7) Write a Python program to print the substring between index values 1 and 4
print(my_str[1:4])

# Practical Example: 8) Write a Python program to print a string from the last character.
print(my_str[-1])

# Practical Example: 9) Write a Python program to print every alternate character from the string starting from index 1.
print(my_str[1::2])


#Functions

def greet(name,msg):
    print(f"Good Morning {name} with greetings {msg}")

greet("World","Good Morning")

#Default Arguments

def greet(name,msg="Good Morning"): #Make default argument at last
    print(f"Good Morning {name} with greetings {msg}")

greet("World","nice Noon")
greet("Hello")

#Keywords Arguments (**kwargs)

def greet(**kwargs):
    if kwargs:
        print(f"HEllo {kwargs['name']} with greetings {kwargs['greet']}")
  
greet(name="Hello World",greet="Nice Noon")

#Arbitary Arguments

def greet(*names):
    for name in names:
        print(f"Hello  {name}")

greet("HEllo","world","This")

#Recusrsion ==> Function calling itself with reduced parameters are known as recusrsion
# def fibo(num):
#     if num <=1 :
#         return num
#     else:
#         return (fibo(num-1) + fibo(num-2))

# num_input = int(input("Enter the number: "))
# if num_input <=0:
#     print("Enter positive numbers!!")
# else:
#     print("Fibonacci series!!!!!!!!!!!")
#     for i in range(num_input):
#         print(fibo(i))


#============================================================================================
#10. Advanced Python (map(), reduce(), filter(), Closures and Decorators)
#============================================================================================
# highre order functions
#function takes function as a arguments they are known as higher order function

def shout(text): 
    return text.upper() 
  
def whisper(text): 
    return text.lower() 
  
def greet(func): 
    # storing the function in a variable 
    greeting = func("Hi, I am created by a function passed as an argument.") 
    print(greeting)  
  
greet(shout) 
greet(whisper)

#=========================
#map()  ->returns a map objects (iterator)
#map(function,iterator)  => iterator can ve list,tuple etc
#================================
def sqaure(n):
    return n*n

numbers = [1,2,3,4,5]
data = map(sqaure,numbers)
print(data) #give object
print(list(data))

def do_double(n):
    return n*2

my_numbers = (1,2,3,4,5)
data = map(do_double,my_numbers)
print(data)
print(list(data))

#using lambda function
data_1 = map(lambda n:n*2,my_numbers)
print(list(data_1))


#========================================
#filter
#Filter the data we want and remove the remaining data just like the water filter do
#filter(function,iterator)  => iterator can ve list,tuple etc
            # |/
            # return true or false
#====================================================

def filter_function(n):
    return n>10       #It will return true or false

my_filter_list = [1,2,32,14,15,6,7,81,9,0,10,100]
my_new_filter_list = filter(filter_function,my_filter_list)
my_new_filter_list_1 = filter(lambda n:n>10,my_filter_list)

print(list(my_new_filter_list))
print(list(my_new_filter_list_1))


#===================================================
#Reduce
#reduce(func, iterable[, initial])
# its reduces thedata and give the fina output
#===================================================
from functools import reduce

my_reduce_lst = [1,2,3,4,5,6,7]

# my_reduce_lst = [1,2,3,4,5,6,7]
# It will take first two data : 1,2 performopration and give 1+2 = 3
# my_reduce_lst = [3,3,4,5,6,7]
# It will take first two data : 3,3 performopration and give 3+3 = 6
# my_reduce_lst = [6,4,5,6,7]
# It will take first two data : 3,3 performopration and give 6+4 = 10
# my_reduce_lst = [10,5,6,7]

# #and so on it will give final output


def my_sum(x,y):
    return x+y

my_data = reduce(my_sum,my_reduce_lst)
print(my_data)

#using lambda function
#we give x,y and in return we will get x+y
my_data_1 = reduce(lambda x,y : x+y ,  my_reduce_lst)
print(my_data_1)

#====================================================
# Introduction to closures and decorators.
#=====================================================
#Decorators => Function returns a function

def greet(fun):
    print("Good Morning")
    fun()
    print("Thanks")

@greet  #decorator
def hello():
    print("Hello all")

def ok():
    print("ok")

def greet_again(fun):
    #Closures
    def func_1():
        print("Good Morning----------")
        fun()
        print("Thanks--------")
    return func_1()

@greet_again  #decorator
def hello():
    print("Hello all")

#OR
greet(ok)

# Write a Python program to apply the map() function to square a list of numbers.
my_list_map = [1,2,3,4,5]
my_list_data = map(lambda x:x*x , my_list_map)
print(list(my_list_data))

# Write a Python program that uses reduce() to find the product of a list of numbers.
my_list_reduce = [1,2,3,4,5]
my_list_data = reduce(lambda x,y : x*y , my_list_reduce)
print(my_list_data)

# Write a Python program that filters out even numbers using the filter() function.
my_list_filter = [1,2,3,4,5]
my_list_data = filter(lambda x : x%2 == 0 , my_list_filter)
print(list(my_list_data))

#Simple Calculator

# def add(a,b):
#     return (f"The addition of {a} and {b} is {a+b}")

# def sub(a,b):
#     return (f"The subtraction of {a} and {b} is {a-b}")

# def mul(a,b):
#     return (f"The multiplication of {a} and {b} is {a*b}")

# def div(a,b):
#     return (f"The division of {a} and {b} is {a/b}")

# print("Please Eneter the number accordingly:\n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division")
# choice = int(input("Enter the choice: "))
# num1 = int(input("Enter the number 1: "))
# num2 = int(input("Enter the number 2: "))

# if choice == 1:
#     data = add(num1,num2)
#     print(data)
# elif choice == 2:
#     data = sub(num1,num2)
#     print(data)

# elif choice == 3:
#     data = mul(num1,num2)
#     print(data)

# elif choice ==4 :
#     try:
#         data =div(num1,num2)
#         print(data)
#     except Exception as e:
#         print(f"The exception error is : {e}")

# else:
#     print("Enter the proper number between 1 to 4")

# Sorting and reversing a list using sort(), sorted(), and reverse().
numbers = [1,21,32,40,15,6]
numbers.sort()
print(numbers)


numbers = [10,121,232,940,315,6]
a  = sorted(numbers)
print(a)

numbers = [7,4,2,7,3,1]
numbers.sort(reverse= True)
print(numbers)

#Write a Python program to insert elements into an empty list using a for loop and append().
lst = []
for i in range(10):
    lst.append(i)
print(lst)

#7) Write a Python program to convert a list into a tuple
lst = [1,2,3,4]
my_tup = tuple(lst)
print(type(my_tup))

#8) Write a Python program to create a tuple with multiple data types.
my_tuple = tuple()
print(type(my_tuple))
print(my_tuple)
#wecannot add data in the tuple

#9) Write a Python program to concatenate two tuples into one.
t1= (1,2,3)
t2=(4,5,6)
t3 = t1+t2
print(t3)

#Write a Python program to access the value of the first index in a tuple.
print(t3[0])

#Write a Python program to access values between index 1 and 5 in a tuple.
print(t3[1:5])

#Write a Python program to access alternate values between index 1 and 5 in a tuple.
print(t3[1:5:2])

#12) Write a Python program to access the value from the last index in a tuple
print(t3[-1])

#
key = [1,2,3]
values = ['apple','mango','banana']

my_dict = dict(zip(key,values))
print(my_dict)

#Counting occurrences of characters in a string using dictionaries
def count_characters(string):
    count_dict = {}
    for i in string:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    return count_dict


my_string = "Good Morning Guyss"
my_dict = count_characters(my_string)
print(my_dict)

#LAmbda duntions are annoymous function thatis function without a name
# ex:- 
x = lambda x : x**2
print(x(10))

x = lambda a,c,b : a+b+c
print(x(1,2,3))

#9. Modules
#=========================================

# import module_6
# from module_6 import my_name,do_squares
# print(my_name)

# print(do_squares(2))
def my_name():
    print("My name is helo world")

def do_squares(n):
    return n*2

import random
list1 = [1, 2, 3, 4, 5, 6]
print(random.choice(list1))
print(random.random())
random.seed(5)
print(random.random())  #0.6229016948897019 will always get seed of 5 as this number


mylist = ["apple", "banana", "cherry"]

print(random.choices(mylist, weights = [10, 1, 1], k = 14))
#apple -> 10 times min
#banana min 1 time
#cherry min 1 time

#total list of length will be 14

print(random.choices(list1))
random.shuffle(list1)
print(list1)
print(random.randint(1,101)) #includes both start and stop value
print(random.randrange(10,100,10)) # inclueds start but nit stop

import math 
print(math.pi) #3.141592653589793
print(math.e) #2.718281828459045
print(math.ceil(9.3)) #10
print(math.floor(9.3)) #9
print(math.pow(3,2)) #3**2 # 9
print(math.sqrt(25)) # 5
print(math.log(10)) #2.302585092994046
print(math.factorial(7)) #5040

#3. Opening and Closing Files
f = open("demofile.txt", "r")
# print(f.read())
#print(f.read(5)) # read first 5 characters
print(f.readline())
print(f.readline())
print(f.readline())

for i in f:
    print(i)

f.close()

# for i in f:
#     print("--------------",i)
#ValueError: I/O operation on closed file.

#r for read file
# a append at last of file
#w will over write evry content
f = open("demofile.txt", "a")
f.write("This data will appendat the last")
print(f.close())


f = open("demofile.txt", "r")
print(f.read())
f.close()

f = open("demofile.txt", "w")
f.write("ok thisis data \n ok")
f.close()


f = open("demofile.txt", "r")
print(f.read())

#f =open("new_file.txt","x") 
#f =open("new_file_1.txt","x")  #create anewfile


#r+ ==> read and write in file
f = open("new_file_1.txt","r+")
f.write("hellloooo")
print(f.read())
f.close()

#w+ ==> add reads to existing write mode
f=  open("new_file_1.txt","w+")
f.write("1")
f.write("2")
print(f.read())
f.close()

try:
    f=  open("new_file_1.txt","w+")
    f.write("1")
    f.write("2")
    print(f.read()) 
except:
    print("ok")
finally:
    f.close()

#Another way of reading and writing
with open ("new_file_1.txt","w+") as f:
    f.write("hello world \n")
    f.write("Welcome")
    # f.seek() # move cursor to the begining
    f.seek(4) # move cursor to 5th position
    lines = f.read()
    print(lines)

# for i in lines:
#     print(i)
#a+  append,read

with open('file.txt', 'a+') as f:
    f.write("4")
    lines = f.read()
    print(lines)
    len_line = f.readline()
    print(len_line)
    print(len(len_line))

with open('file_1.txt','w+') as f:
    f.write("ok")

# with open('file_2.txt','r+') as f:
#     f.write("ok")
#It ill throw error

#If the file exists, w+ truncates the file and opens it; a+ opens it without truncating.
#readline() reads and returns a single line from a file, while readlines() reads all lines in a file and returns them as a list of strings, with each list item representing one line.


f = open("file.txt","w+")
my_data = ['apple','mango']
for i in my_data:
    f.write(f"My name is {i}\n")
    f.seek(0)
print(f.read())

f = open("file.txt","w+")
my_data = ['apple','mango']
lst = []
for i in my_data:
    lst.append(i)
f.writelines(lst)
print(f.read())
print(f.tell()) # tell the current cursor posotion

#Exception handling

a = 10
b = 0
#print(a/b) #ZeroDivisionError: division by zero
try:
    print(a/b)
except Exception as e:
    print("excepetion:",e)
finally:
    print("Done")


try:
    a = 10
    b=0
    print("the resut is :",a//b)
except ZeroDivisionError:
    print("You got zero dovidon error")
except ValueError:
    print('you gotvalue Error')
except Exception as e:
    print("Exception:------",e)
else:
    print("you got nothing")
finally:
    print("Finally")

try:
    a = 10
    b=9
    c
    print("the resut is :",a//b,c+a)
except ZeroDivisionError:
    print("You got zero dovidon error")
except ValueError:
    print('you gotvalue Error')
except Exception as e:
    print("Exception:------",e)
else:
    print("you got nothing")
finally:
    print("Finally")


class MyCustomError(Exception):
    def __init__(self,error,error_code):
        self.error = error
        self.error_code = error_code
        print(f"You got the error {self.error} with code {self.error_code}")


def divide(a, b):
    if b == 0:
        raise MyCustomError("Division by zero is not allowed", 400)
    return a / b


try:
    a = divide(1,0)
    print(a)
except MyCustomError as e:
    print("e------->",e)


#10. Search and Match Functions
import re

text = "Hello, welcome to Python world!"
search = re.search(r"Python", text) # search in the entire string
print("search:",search)
if search:
    print("search found")
else:
    print("No search found")

match = re.match(r"He",text) #searches at thestarting of te string
print("match:",match)
if match:
    print("match found")
else:
    print("No match found")

pattern = r"\d+"  # Matches one or more digits
text = "Hello 7854 number is 12345"
match = re.search(pattern, text)
print(match.group())  # Output: 12345

#OOPS
#Inheritance

class Employee:
    #Constructor
    #When object is initilaized the constructor is called first
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def showDetails(self):
        print(f"the name of employee is {self.name} and age is {self.age}")

class Programmer(Employee):
    def __init__(self,name,age,lang):
        super().__init__(name,age) #Overiding init method with super keyword
        self.lang = lang
    def company_data(self):
        print("Company data in program class")
    def showProgram(self):
        print("I will do python program")
    
    def showlang(self):
        print(f"I will do {self.lang} program")

class Company(Programmer):

    def company_data(self):
        print("Company data in company class")

    def show_company(self):
        super().company_data()

a = Employee("Meera","98268")  #object of class
print(a.name)  # accessing variables of class
print(a.age)
a.showDetails()  #accessing methids of class

b = Employee("Rathod","96544")
b.showDetails()

c = Programmer("Raj","7546","Html")
c.showProgram()

d= Programmer("Rohan","8546",'Java')
d.showlang()

e=Company("Rohit","9546",'CSS')
e.company_data()
e.show_company()

#Method overloading => Compile time polymorphism
def add(datatype,*args):
    if datatype == 'int':
        ans = 0
        for i in args:
            ans+=i
        print("Ans :-",ans)
    if datatype == 'str':
        ans =''
        for i in args:
            print(i)
            print(ans)
            ans+=i
        print("Ans in string ",ans)

add('int',1,2,3,4)
add('str',"apple","mango","banana")

#Dunder methods or magic methods
#they are defined in class
#__init__

class Employee:
    name= "Hello"

    def __len__(self):
        i=0
        for c in self.name:
            i+=1
        return i

e = Employee()
print(e.name)
print(len(e))  # it is a dunder method


class Employee:
    def __init__(self,name):
        self.name = name

    def __len__(self):
        i=0
        for c in self.name:
            i+=1
        return i

    def __str__(self):
        return f"My name is {self.name} str"

    def __repr__(self):
        return f"My name is {self.name} repr"

    def __call__(self):
        return "Hello i am good"

    #it there in not str then it will go to repr

e = Employee("Helloooo")
#print(e) #without __str__  #<__main__.Employee object at 0x00000243A8170A90>
print(e) #with __str__   My name is Helloooo
print(str(e))
print(repr(e))
print(e()) # --> call function
print(e.name)
print(len(e))  # it is a dunder method


#Method Overiding --> acces methods of parent to child
class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

class Circle(Shape):
    def __init__(self,radius):
        #    for calling this    print(super().area()) #calling the area of parent class
        # we have to call the super init
        super().__init__(radius,radius)
        self.radius = radius

    def area(self):
        print(super().area()) #calling the area of parent class
        return 3.14*self.radius*self.radius

rectangle = Shape(3,5)
print("The area of rectangle is:",rectangle.area())

circle = Circle(4)
print("The area of circle is:" , circle.area())

#operator overloading
class Vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

    #print(v1+v2) #TypeError: unsupported operand type(s) for +: 'Vector' and 'Vector'
    # to resolve this issue we have to create a add funtion

    def __add__(self,x):
        #Will return the string
        #return f"{self.i +x.i}i + {self.j + x.j}j + {self.k + x.k}k"
        return Vector(self.i+x.i,self.j+x.j,self.k+x.k)
v1 = Vector(1,2,3)
print(v1)

v2 = Vector(4,5,6)
print(v2)

#print(v1+v2) #TypeError: unsupported operand type(s) for +: 'Vector' and 'Vector'
#after defing the add function

print(v1+v2)
print(type(v1+v2)) # class str
print(type(v1))

#now i want to get the result of two vector as vector then

#Inheritance
# ->Single
# ->multiple
# ->multilevel
# ->heriachial
# ->hybrid
# 1-Single
class Parent:
    def func1(self):
        print("This func is in parent class.")
  
class Child(Parent):
    def func2(self):
        print("This func is in child class.")
 
object = Child()
object.func1()
object.func2()

#Multiple Inheritance: 
class GrandParent:
    def func1(self):
        print("This func is in GrandParent class.")
        print("Self.Grand Parent Name",{self.grand_parent})

    def show(self):
        print("hello in GrandParent")

class Parent:
    def func2(self):
        print("This func is in Parent class.")
        print("Self. Parent Name",{self.parent})

    def show(self):
        print("hello in Parent")

class Child(GrandParent,Parent):
    def func3(self):
        print("This is child class" , {self.grand_parent},{self.parent})

c = Child()
c.grand_parent = "Grand"
c.parent = "Parent"
c.func1()
c.func2()
c.func3()
c.show() #hello in GrandParent  -- becasue GrandParent class is inherit first

print(Child.mro()) #method resolution order
# [<class '__main__.Child'>, <class '__main__.GrandParent'>, <class '__main__.Parent'>, <class 'object'>]

#multilevel Inheritance
class GrandParent:
    def func1(self):
        print("This func is in GrandParent class.")
        print("Self.Grand Parent Name",{self.grand_parent})

    def show(self):
        print("hello in GrandParent")

class Parent(GrandParent):
    def func2(self):
        print("This func is in Parent class.")
        print("Self. Parent Name",{self.parent})

    def show(self):
        print("hello in Parent")
        GrandParent.show(self)

class Child(Parent):
    def func3(self):
        print("This is child class" , {self.grand_parent},{self.parent})


c = Child()
c.grand_parent = "Grand"
c.parent = "Parent"
c.func1()
c.func2()
c.func3()
c.show()

#Herirachial inheritance

class A:
    def a_show(self):
        print("A")


class B(A):
    def b_show(self):
        print("B")

class C(A):
    def c_show(self):
        print("C")

c = C()
c.c_show()
c.a_show()
print(C.mro())

b = B()
b.b_show()
b.a_show()

#hybrid inheritance
#when we use more than one inheritance

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B,A):
    pass

d = D()
print(D.mro())

#Plymorphism
#ability to take varoius form
# ->operator level polymorphism/
#1+2 ==> addition
#"abc"+"def"  ==> Concatatation


# ->Function level polymorphism
# len([1,2,4])
# len({1,2,3})
# len("abfdfghd")

# ->class Level polymorphism

class A:
    def p(self):
        return "Function in p in A"

class B:
    def p(self):
        return "Function in p in B"

a = A()
print(a.p())

b=B()
print(b.p())

for i in a,b:
    print(i.p())


#Abstarction in python

#python does not directly support Abstraction
#we have to use ABC class
# (Abstarct Base Class)
# we cannot access abstract class directly 
from abc import ABC,abstractmethod
class Computer(ABC):
    @abstractmethod
    def process(self):
        return "Running"

    @abstractmethod
    def process_1(self):
        print("a")


class Computer_1(Computer):
    @abstractmethod
    def process(self):
        return ("Computer_1")

# com = Computer()
# print(com.process())


class Mouse(Computer):
    def process(self):
        return "Running in mouse"

    def process_1(self):
        return "process_1"

    def show(self):
        return "Mouse Works"

mouse = Mouse()
print(mouse.process())
print(mouse.process_1())

print(mouse.__dir__())


#Encapsulation
#bundling of data (attributes) and methods (functions) that operate on the data into a single unit or class.
# It also involves restricting direct access to some of an object's components,

class BankAccount:
    def __init__(self,name,salary,age):
        self.name = name  #public
        self._salary = salary #proteced  only use within class and subclass
        self.__age = age #private

    def set_salary(self):
        self._salary = 78399
        return f'{self._salary}'

class BankAccountHolder(BankAccount):
    def show_holder(self):
        return f"{self._salary} in class BankAccountHolder "

bank_account = BankAccount("Rohan",2000,56)
print(bank_account._salary)

# print(bank_account.__age) # you can not directly access the private data like this it will thorw you error
print(bank_account._BankAccount__age) # we can accessit like this

print(bank_account.name)

print(bank_account.set_salary())

bank_account_holder = BankAccountHolder("Rita",893300,89)
print(bank_account_holder.show_holder())


