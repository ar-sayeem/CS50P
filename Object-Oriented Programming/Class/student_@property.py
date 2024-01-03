# @property
# decorators

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house


    def __str__(self):
        return f"{self.name} is from {self.house}"


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name
    

    @property
    def house(self):            # always 1 argument
        return self._house

    @house.setter
    def house(self, house):     # self argument always & others
        if house not in ["Griffindor", "Hufflepuff", "Revenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self._house = house


def main():
    student = get_student()

    # student._house = "Mirpur"       # will work
    # student.house = "Mirpur"        # won't work

    # getter & setter: to make sure programmers can't do things
    # like student.house = "..." to set a value mennually at will
    # getter & setter give more control over objects

    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
  main()