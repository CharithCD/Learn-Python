# Ask the user for their name and greet them with their name.
name = input("What is your name?: ").strip().title();

#Using split
firstName, lastName = name.split(" ");

print(f"Welcome {firstName}");