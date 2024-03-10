class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def main():
    student = get_Student()
    print(student.name)
    print(student.age)

def get_Student():
    name = "John"
    age = 25
    student = Student(name, age)
    return student

if __name__ == '__main__':
    main()