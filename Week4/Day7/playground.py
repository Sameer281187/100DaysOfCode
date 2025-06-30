def add(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

print(add(7, 8))
print(add(2,3,4))
print(add(2,3,4,5,6,7,8))