# converting a number/ string to bool datatype
print(bool(0))

#Notice below 2 statements return True
print(bool("True"))
print(bool("False"))

#Notice below 2 statements return True
print(bool('T'))
print(bool('F'))

# converting string to integer
print(int("123"))

# The below line will give an error as typecasting cannot convert invalid arguments in the desired data type
# print(int("True"))

# Converting integer to string. Almost everything can be converted to string without an error
print(str(1234))

# Converting integer to float and vice versa
print(int(123.45))
print(float(123))