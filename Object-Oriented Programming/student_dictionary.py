def main():
    student = get_student()
    if student["name"] == "Padma":      # Override dictionary
      student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")

def get_student():
  name = input("Name: ")
  house = input("House: ")
  return {"name": name, "house": house}


"""
    student = {}          # Empty dictionary initial
    student["name"] = input("Name:")
    student["house"] = input("House: ")
    return student        # return dictionary
"""

if __name__ == "__main__":
  main()
