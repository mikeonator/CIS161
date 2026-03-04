# Michael Audi - CIS161 Week 9 Main Assignment

class Students:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def hello(self):
        print(f"Hello, my name is {self.name}. I'm {self.age} years old, and I'm in grade {self.grade}!")

class Staff:
    def __init__(self, name, role, department, salary):
        self.name = name
        self.role = role
        self.department = department
        self.salary = salary

class Teacher(Staff):
    def __init__(self, name, age, role, department, salary):
        super().__init__(name, role, department, salary)
        self.age = age
    
    def hello(self):
        print(f"Hello, my name is {self.name}. I'm {self.age} years old, and I'm a {self.role} in the {self.department} department. My salary is {self.salary}!")

class Square:
    def __init__(self, name, side):
        self.name = name
        self.side = side
    
    def area(self):
        print(f"The area of square {self.name} is {(self.side)**2}")
    
    def perimeter(self):
        print(f"The perimeter of square {self.name} is {4*(self.side)}")

def main():
    # Step 1
    print(f"----- Step 1 -----")
    stu_raj = Students("Raj",16,11)
    stu_joe = Students("Joe",17,11)

    stu_raj.hello()
    stu_joe.hello()

    # Step 2
    print(f"\n----- Step 2 -----")
    tea_james = Teacher("James",32,"Teacher","Computer Science",80000)
    tea_chris = Teacher("Chris",41,"Teacher","Music",80000)

    tea_james.hello()
    tea_chris.hello()

    # Step 3
    print(f"\n----- Step 3 -----")
    square_1 = Square("1",10)
    square_2 = Square("2",20)

    square_1.area()
    square_1.perimeter()
    square_2.area()
    square_2.perimeter()

if __name__ == "__main__":
    main()