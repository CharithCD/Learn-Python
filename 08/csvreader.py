import csv

users = [
    {
        'name': 'John',
        'age': 30,
        'address': '123 Main St, Apt 1'
    },
    {
        'name': 'Jane',
        'age': 25,
        'address': '456 Elm St, Apt 2'
    },
    {
        'name': 'Joe',
        'age': 28,
        'address': '789 Oak St, Apt 3'
    }
]

# with open('names.csv', 'w') as file:
#     writer = csv.writer(file)
#     writer.writerow(['name', 'age', 'address'])
#     for user in users:
#         writer.writerow([user['name'], user['age'], user['address']])
#     file.close()

newuser=[]

# with open('names.csv', 'r') as file:
#     reader = csv.reader(file)
#     for name, age, address in reader:
#         newuser.append({
#             'name': name,
#             'age': age,
#             'address': address
#         })
#     print(newuser)
#     file.close()

with open('names.csv', 'r') as file:
    reader = csv.DictReader(file)
    for user in reader:
        print(user)
    file.close()

