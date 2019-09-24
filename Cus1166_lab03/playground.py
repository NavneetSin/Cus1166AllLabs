print("Practicing Variables")
# Here add the commands you practice and their corresponding output i.e...
myvar = 1
print(f"Variable myvar : {myvar} is an {type(myvar)}")
# ... rest of your practice code.
print("Done Practicing Variables")

print('print and input command')

print("Hello Word")  # Display a message
# Get user input and display a message.
myname = input("What is your name: ")
print("Hello " + str(myname))
# Alternative way to format a string
print("Hello %s" % myname)

print("")
print("")
print("Initializing variables in pythons")
i = 120
print(f"Variable i has the value {i}")
f = 1.6180339
print(f"Variable f has the value {f} and its type is {type(f)}")
b = True
print(f"Variable b has the value {b}")
n = None
print(f"Variable n has the value of {n}")
# tuple
c = (10, 20, 10)
print(f" c[0] has the value {c[0]} and is of type: {type(c)}")
# list
l = ["Anna", "Tom", "John"]
l = [10, 20, 30]
print(f" l[0] has the value {l[0]} and is of type: {type(l)}")
# Sets variables.
s = set()
s.add(1)
s.add(4)
s.add(6)
print(s)
print("")
print("Using Dictionary")
grades = {"Tom": "A", "Mark": "B-"}
grades["Tom"]
grades["Anna"] = "F"
# Create an empty dictionary .
mydictionary = dict()
print(grades)
print(mydictionary)

print("")
print("")
print("Using conditionals")

print("Lets check what is the sign of you number!!")
number = input("Choose a number: ")
number = int(number)
if (number > 0):
    print("The number x is positive")
elif (number < 0):
    print("The number x is negative")
else:
    print("The number x is zero")

print("")
print("")
print("Using Loops")

for i in range(5):
    print(i)
for i_idx, i_value in enumerate(range(2, 10)):
    print(f"{i_idx} - {i_value}")

print("Defining and using functions")

print("Lets check if the number you enter is_even!!")
number = input("Choose a number: ")
number = int(number)

def is_even(number):
    if (number % 2) == 0:
        return True
    else:
        return False
print(is_even(number))
print("")
print("")
print("Defining Classes")
