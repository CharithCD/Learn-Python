def main():
    name = input("What is your name? ").strip().upper();
    PrintName(name);


def PrintName(name = "World"):
    print("Hello, " + name + "!");

if __name__ == "__main__":
    main();