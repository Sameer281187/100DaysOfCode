count = 0

def increase_count(value):
    count = value + 1
    print(f"Count = {count}")

def set_count():
    count = 1
    print(f"Count = {count}")

set_count()
print(f"Count = {count}")

increase_count(count)
print(f"Count = {count}")

"""
The value of variable count remains different at global and local level. Even though the count value is being 
modified by the 2 functions, the count variable at the global level remains unchanged
"""