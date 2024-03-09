x = int(input("Enter a number: "));
y = int(input("Enter another number: "));

if x > y:
    print(x, "is greater than", y);

if x < y:
    print(x, "is less than", y);

if x == y:
    print(x, "is equal to", y); 

if x != y:
    print(x, "is not equal to", y);

if x >= y:
    print(x, "is greater than or equal to", y);

if x <= y:
    print(x, "is less than or equal to", y);


# elif
if x > y:
    print(x, "is greater than", y);
elif x < y:
    print(x, "is less than", y);
else:
    print(x, "is equal to", y);

#or
if x < y or x > y:
    print("x is not equal to y");
else:
    print("x is equal to y");