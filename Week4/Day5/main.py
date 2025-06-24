with open("file1.txt") as file1:
    list1 = file1.readlines()

with open("file2.txt") as file2:
    list2 = file2.readlines()
common_elements = [str for str in list1 if str in list2]
result = [int(item.strip('\n')) for item in common_elements]

print(result)