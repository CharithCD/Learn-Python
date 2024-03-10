import sys
import os

names = []

# for _ in range(3):
#     name = input('Enter a name: ')
#     names.append(name)
#     open('names.txt', 'a').write(name+'\n')


#     # with open('names.txt', 'a') as file:
#     #     file.write(name+'\n')
#     #     file.close()

# print('The names are', names)

# with open('names.txt', 'r') as file:
#     for name in file:
#         names.append(name.strip())
#     file.close()
#     print('The names are', names)

# with open('names.txt', 'r') as file:
#         lines = file.readlines()

# for line in lines:
#         line = line.strip()
#         names.append(line)

# print('The names are', names)


# with open('names.txt', 'r') as file:
#     for name in file:
#         names.append(name.strip())
#     file.close()
#     print('The names are', names)

users = [
    {
        'name': 'John',
        'age': 30
    },
    {
        'name': 'Jane',
        'age': 25
    },
    {
        'name': 'Joe',
        'age': 28
    }
]

# with open ("names.csv", "a") as file:
#     for user in users:
#         file.write(f"{user['name']}, {user['age']}\n")
#     file.close()

# with open("names.csv", "r") as file:
#     for line in file:
#         name, age = line.strip().split(',')
#         print(f"{name} is {age} years old")
#     file.close()

#look into sorting the names in the file