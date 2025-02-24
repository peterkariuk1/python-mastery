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
  
  #COMPARISON OPERATORS IN PYTHON
  > -- GREATER THAN
  < -- LESS THAN
  <= -- LESS/EQUAL TO
  >= -- GREATER/EQUAL TO
  == -- EQUAL TO
  != -- NOT EQUAL TO
