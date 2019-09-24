from myModules.models import Student
from myModules.math_utils import average_grade

if __name__ = "main":
    roster_of_students = [
        Student("Asaib",68),
        Student("Chimp",93),
        Student("Sainx",89),
        Student("Thollusk",88),
        Student("Bijiaf",94),
        Student("Mituya",75),
        Student("Fintio",100),
        Student("Mookkaug",45),
        Student("Thoshner",79),
        Student("Op",86),
    ]
    for item in roster_of_students:
        item.print_student_info()
    print("The Roster's Average is " + str(average_grade(roster_of_students)))
