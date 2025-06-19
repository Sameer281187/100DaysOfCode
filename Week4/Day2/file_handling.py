# new_file = open("my_file.txt")
# content = new_file.read()
# print(content)
# new_file.close()

# with open("my_file.txt") as new_file:
#     content = new_file.read()
#     print(content)

with open("../../Resources/my_file.txt", "a") as new_file:
    new_file.write("Added new content. ")