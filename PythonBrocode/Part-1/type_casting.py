name = "Haraf Rubena"
age = 34
gpa1 = 3.14
gpa2 = 3.9
is_working = True

# type function : to fin the data type of a variable 
print(type(name)) #<class 'str'>
print(type(age)) #<class 'int'>
print(type(gpa1)) #<class 'float'>
print(type(is_working)) #<class 'bool'>

# float to int
print(int(gpa1)) #3
print(int(gpa2)) #3

# int to float
print(float(age)) #34.0

# int to str
new_age = str(age)
print(new_age) #34
print(type(new_age)) #<class 'str'>

# string to bool
name = bool(name)
print(name) #True