msg = "Hello World"

print(msg)




#   Python Variables - Creating Variables
#   https://www.w3schools.com/Python/python_variables.asp
#   https://www.w3schools.com/Python/trypython.asp?filename=demo_variables1

# "A variable is created the moment you assign a value to it."" 

x = 3
y = "Hannah"

print(x)
print(y)




#   Python Variables - Creating Variables
#   https://www.w3schools.com/Python/python_variables.asp
#   https://www.w3schools.com/Python/trypython.asp?filename=demo_variables2

# "Variables do not need to be declared with any particular type"
# "The variable's type may even be changed after the variable has been set"

a = 4
a = "Fredrick"

print(a)




#   Python Variables - Casting
#   https://www.w3schools.com/Python/python_variables.asp
#   https://www.w3schools.com/Python/trypython.asp?filename=demo_variables_casting

# "If the data type of a variable needs to be specified, that specification can be done through Casting"

e = str(3)
f = int(4)
g = float(4)

print(e)
print(f)
print(g)




#   Python Variables - Get The Type
#   https://www.w3schools.com/Python/python_variables.asp
#   https://www.w3schools.com/Python/trypython.asp?filename=demo_variables_type

# "A user may get the data type of a variable using the type() function"

j = 5
k = "Jacob Fernandez"

print(type(j))
print(type(k))




#   Python Variables - Case-Sensitive
#   https://www.w3schools.com/Python/python_variables.asp
#   https://www.w3schools.com/Python/trypython.asp?filename=demo_variables_cs

# "Variable names are case-sensitive."

h = 4
H = "Alexander The Great"

print(h)
print(H)




#   Python Variables - Variable Names
#   https://www.w3schools.com/Python/python_variables_names.asp
#   https://www.w3schools.com/Python/trypython.asp?filename=demo_variable_names_legal

# "A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Three rules for python variables:-
#  (1) A variable name must start with a letter or the underscore character.
#  (2) A variable name cannot start with a number.
#  (3) A variable name can only contain alpha-numeric characters and underscores.
#  (4) Variable names are case-sensitive (age, Age and AGE are three different variables)."

myvar = "Alpha"
my_var = "Bravo"
_my_var = "Charlie"
myVar = 'Delta'
MYVAR = "Echoe"
myvar2 = "Foxtrot"

print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)




#   Python Variables - Variable Names - Multi Words Variable Names - Camel Case
#   https://www.w3schools.com/Python/python_variables_names.asp

# "Each word,except for the first word, starts with a capital letter."

myVariableName = "Golf"




#   Python Variables - Variable Names - Multi Words Variable Names - Pascal Case
#   https://www.w3schools.com/Python/python_variables_names.asp

# "Each word, from the first to third words, starts with a capital letter."

MuyVariableName = "Hotel"




#   Python Variables - Variable Names - Multi Words Variable Names - Snake Case
#   https://www.w3schools.com/Python/python_variables_names.asp

# "Each word is separated by an underscore character."

my_variable_name = "India"




#   Python Variables - Assign Multiple Values - Many Values to Multiple Variables
#   https://www.w3schools.com/Python/python_variables_multiple.asp
#   https://www.w3schools.com/Python/trypython.asp?filename=demo_variables8

# "Python allows the user to assign values to multiple variables with a single line."

x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)




#   Python Variables - Assign Multiple Values - One Value to Multiple Variables
#   https://www.w3schools.com/Python/python_variables_multiple.asp
#   https://www.w3schools.com/Python/trypython.asp?filename=demo_variables6

# "THe same value can be applied to multiple values using a single line of syntax."

e = r = t = "Strawberry"

print(e)
print(r)
print(t)




#   Python Variables - Assign Multiple Values - Unpack a Collection
#   https://www.w3schools.com/Python/python_variables_multiple.asp
#   https://www.w3schools.com/Python/trypython.asp?filename=demo_variables_unpack

# "Given a collection of values in a list, or tuple, Python allows the user to extract the values into variables. This process is called Unpacking."

fruits = ["apple", "banana", "chocolate"] 
v, b, n = fruits

print(v)
print(b)
print(n)




#   Python Variables - Output Variables 
#   https://www.w3schools.com/Python/python_variables_output.asp
#   https://www.w3schools.com/Python/trypython.asp?filename=demo_variables3

# "The Python print statement is often used to create an output of variables. To combine both grammar-based text and a variable, the 'plus' character is used in Python."

a = "really good !"

print("Python is " + a)




#   Python Variables - Output Variables
#   https://www.w3schools.com/Python/python_variables_output.asp
#   https://www.w3schools.com/Python/trypython.asp?filename=demo_variables4

# "The 'plus' character may also be used to add one variable to another variable."

s = "Python is "
d = "really really good."
a = s + d

print(a)




#   Python Variables - Output Variables
#   https://www.w3schools.com/Python/python_variables_output.asp
#   https://www.w3schools.com/Python/trypython.asp?filename=demo_variables5

# "In terms of numbers, the 'plus' character works as a function within a mathematical equation."

q = 5
w = 2

print(q + w)




#   Python Variables - Global Variables 
#   https://www.w3schools.com/Python/python_variables_global.asp
#   https://www.w3schools.com/Python/trypython.asp?filename=demo_variables_global

# "Create a variable outside of a function, and then use that variable inside the function."

p = "fantastic"

def myfunc():
    print("Life is " + p + " !")

myfunc()




#   Python Variables - Global Variables
#   https://www.w3schools.com/Python/python_variables_global.asp
#   https://www.w3schools.com/Python/trypython.asp?filename=demo_variables_global2

# "If a variable is created iwth the same name - iside a function - this variable will be 'local' in nature."
# "The variable may only be used inside its function."
# "The global value with the same name will remain as it was - 'global' in nature and with the original value."

o = "pretty good !"

def myfunc():
    o = "beautiful."
    print("Singapore is " + o)

myfunc()

print("Singapore is " + o)




#   Python Variables - Global Variables
#   https://www.w3schools.com/Python/python_variables_global.asp
#   https://www.w3schools.com/Python/trypython.asp?filename=demo_variables_global3

# "To create a global variable inside s function, the 'global' keyword may be used."
# "If the 'global' keyword isused, the variable belongs to the 'global' scope."

def myfunc():
    global l
    l = "easy"

myfunc()

print("Learning Hyper Text Markup Language is " + l + " !")




#   Python Variables - Global Variables
#   https://www.w3schools.com/Python/python_variables_global.asp
#   https://www.w3schools.com/Python/trypython.asp?filename=demo_variables_global4

# "The keyword- global - may be used if the user wants to change a global variable which is inside a function."
# "To change the value of a global variable inside a function, make a reference to tge variable by using the global keyword."

e = "good old days !"

def myfunc():
    global e
    e = "olden times."

myfunc()

print("The year 2019 are the " + e)