def main():
    sayHello("John")
    sayGoodBye("John")

def sayHello(name):
    print("hello, my name is", name)

def sayGoodBye(name):
    print(f"Good Bye, {name}")

if __name__ == "__main__":
    main();