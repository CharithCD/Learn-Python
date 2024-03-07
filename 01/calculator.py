# # int
# x = int(input("Enter a number: "));
# y = int(input("Enter another number: "));
# print(x + y);

# # float
# x = float(input("Enter a number: "));
# y = float(input("Enter another number: "));
# print(int(x + y));
# print(round(x + y));
# print(round((x + y), 9));
# print(round((x + y), 2));
# print(round((x + y), 1));


#Number formatting with f strings
a = 1000000;
print(f"{a:e}"); # scientific notation
print(f"{a:,}"); # add comma to the number
