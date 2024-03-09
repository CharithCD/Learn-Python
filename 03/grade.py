score = int(input("Score: "))

if score >= 90 and score <= 100:
    print("A");
elif score >= 80 and score < 90:
    print("B");
elif score >= 70 and score < 80:
    print("C");
elif score >= 60 and score < 70:
    print("D");
else:
    print("F");


def isEven(n):
    return "Even" if n % 2 == 0 else "Odd"

# The code above is a simple grade calculator. It takes a score as input and prints the corresponding grade.