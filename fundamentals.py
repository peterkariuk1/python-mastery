# VARIABLES
# With correct convention and primitive types

course_name = 'IT'  # string
course_code = 23456  # integer
rating = 23.4  # float
is_published = True  # boolean

# strings
greeting = 'Hello World'
print(greeting[4: -4])
# : sign is used as an equivalent of up to and the - sign is used to serve as a slice method for characters in a string

# escape sequences
print("Python \" Programming")
print("Use double backlash to avoid escaping with one \\")
print('I will show you how to move to the next line here \n This is a new line')

# string methods
programming_language = 'JavaScript'
print('Find the length of text:', len(programming_language))
print('To uppercase:', programming_language.upper())
# More string methods @python 3 string methods

# numbers in Python
print(2 + 4)
print(2 - 4)
print(10 * 4)
print(10 / 3)
print(10 // 3)
print(10 % 3)

# Type Conversion
x = input('x: ')
y = int(x) + 1
print(f"x: {x}, y: {y}")

# IF statements

temperature = 26
if temperature > 30:
    # indent always
    print("It's hot, drink water")
elif temperature == 26:
    print("Normal temperature")
else:
    print("It's cold")

    # COMPARISON OPERATORS IN PYTHON

    # > -- GREATER THAN
    # < -- LESS THAN
    # <= -- LESS/EQUAL TO
    # >= -- GREATER/EQUAL TO
    # == -- EQUAL TO
    # != -- NOT EQUAL TO

   # TERNARY OPERATORS

   # for IF statements
student_marks = 38

message = 'Good score!' if student_marks >= 60 else "Need for improvement!"
print(message)


# chaining IF statements

if 60 >= student_marks < 100:  # more readable code for if statements
    print(message, "2")

# LOGICAL operators
# and -- all logic varibles must be true
# or -- atleast one logic variable must be true
# not -- inverses a boolean value if true becomes false

# FOR LOOPS

for number in range(5):
    print('This will print 5 times:', number + 1)

# FOR ELSE LOOPS

successful = True

for number in range(6):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Not successful")

# NESTED LOOPS
    # outer loop
for a in range(5):
    # inner loop
    for b in range(3):
        print(f"({a},{b})")

# WHILE LOOPS
while True:
    command = input("Enter text:")
    print("Echo:", command)
    if command.lower() == "quit":
        break


count = 0
for even_number in range(1,25):
    if even_number % 2 == 0:
        count += 1
        print(even_number)
print(f"We have {count} even numbers")


# print("We have 4 even numbers")
