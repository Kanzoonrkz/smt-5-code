from pprint import pprint
class Person:
  def __init__(self, name, ssn):
    self.name = name
    self.ssn = ssn

class Instructor(Person):
  def __init__(self, target, salary):
    super().__init__(target.name, target.ssn)
    self.salary = salary
    self.students = []
  
  def allStudents(self):
    for i in range(len(self.students)):
      print(str(i+1) + ". " + self.students[i].name)

class Student(Person):
  def __init__(self, target, courses, grades):
    super().__init__(target.name, target.ssn)
    self.courses = courses
    self.grades = grades

class GraduateStudent(Student):
  def __init__(self, target):
    super().__init__(target.name, target.ssn, target.courses, target.grades)

def main():
  print("\nInitiate 4 person:")
  azriel = Person("M. Azriel", "19/STD/220673")
  ija = Person("M. Izzza", "19/STD/787236")
  geo = Person("Geosaby", "16/INS/229853")
  raju = Person("Rajoeoe", "14/ALM/789201")
  pprint(vars(azriel))
  pprint(vars(ija))
  pprint(vars(geo))
  pprint(vars(raju))

  print("\nGeo as Instructor, no students")
  insGeo = Instructor(geo, 8000000)
  pprint(vars(insGeo))

  print("\nAzriel, Izzza and Rajoeoe as Student")
  stdAzriel = Student(azriel, "math", 80)
  stdIja = Student(azriel, "science", 75)
  stdRaju = Student(raju, "Tech", 90)
  pprint(vars(stdAzriel))
  pprint(vars(stdIja))
  pprint(vars(stdRaju))

  print("\nAssign Azriel and Izzza as Geo's student")
  insGeo.students.extend([azriel, ija])
  print("\nGeo's student:")
  insGeo.allStudents()
  
  return

if __name__ == "__main__":
  main()
