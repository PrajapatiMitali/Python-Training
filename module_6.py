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

#my_stirng([start:step:stop])
#it will give start:step:stop-1 
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
for i in range(1,10):
    print(i,end=" ")

print("\n====================================")
for j in range (1,20,2):
    print(j,end=" ")