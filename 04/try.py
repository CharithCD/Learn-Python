# try:
#     num = int(input('Enter a number: '))
#     print(f"Your number is: {num}")
# except ValueError:
#     print('ValueError: Please enter a valid number')
def main():
    print(get_int())

def get_int():
    while True:
        try:
            num = int(input('Enter a number: '))
        except ValueError:
            print('ValueError: Please enter a valid number')
        else:
            return num
        finally:
            print('Thank you for using our service')

def get_int():
    while True:
        try:
            num = int(input('Enter a number: '))
            return num;
        except ValueError:
            print('ValueError: Please enter a valid number')
    
main();