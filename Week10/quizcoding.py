# Michael Audi - CIS161 Week 10 Quiz Coding

class Animal:
    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age

    def print_me(self):
        print(f"{self.name} is {self.age} years old.")

    def speak(self):
        print(f"{self.name} says Noise!")


class Dog(Animal):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def speak(self):
        print(f"{self.name} says Woof!")


class Cat(Animal):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def speak(self):
        print(f"{self.name} says Meow!")


def main():
    Spot = Dog("Spot", 2)
    Mittens = Cat("Mittens", 1)

    Animal.print_me(Spot)
    Dog.speak(Spot)
    Cat.print_me(Mittens)
    Cat.speak(Mittens)

    return


if __name__ == "__main__":
    main()
