# animal = input("Enter an animal: ")
# sound = input("Enter the sound it makes: ")
# rep = int(input("How many times should it be printed? "))


# # while rep != 0:
# #     print(animal, "says", sound, "!")
# #     rep -= 1

# for i in range(rep):
#     print(animal, "says", sound, "!")

# for i in [1, 2, 3, 4, 5]:
#     print(animal, "says", sound, "!")

# users = ["Alice", "Bob", "Charlie", "David", "Eve"];
# print(users);
# for user in users:
#     if user == "Charlie":
#         continue;
#     print("Hello", user);

users = {
    "Alice": 25,
    "Bob": 30,
    "Charlie": 35,
    "David": 40,
    "Eve": 45
}

# print(users["Alice"]);

for user in users:
    print(user, "is", users[user], "years old");