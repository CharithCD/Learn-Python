email = input("Enter your email: ")

username, domain = email.split("@")

# if "@" in email:
#     print("Valid email")
# else:
#     print("Invalid email")

# if username and "." in domain:
#     print("Valid email")
# else:
#     print("Invalid email")

if username and domain.endswith(".edu"):
    print("Valid email")