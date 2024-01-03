class Student:
    def __init__(self, name, house):      # , patronus
        if not name:      # if name = ""
            raise ValueError("Missing name")
        if house not in ["Griffindor", "Hufflepuff", "Revenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self.name = name     # self.n = name
        self.house = house   # self.h = house
        # self.patronus = patronus

    def __str__(self):      # object as string
        return f"{self.name} from {self.house}"
      
    """
    def charm(self):
      match self.patronus:
        case "Stag":
          return "🐴"
        case "Otter":
          return "🦦"
        case "Jack Russell terrier":
          return "🐶"
        case _:
          return "❗❗❗"
        """


def main():
    student = get_student()
    # print(f"{student.name} from {student.house}")
    # print("Expecto Patronus!")
    # print(student.charm())
    print(student)



def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house)      # initialization init  # , patronus

    """
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student
  """


if __name__ == "__main__":
  main()
