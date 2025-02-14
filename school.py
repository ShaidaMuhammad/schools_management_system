from class_ import Class
from person import Student, Teacher

class School:
    """
    Represents a school that manages students, teachers, and classes.
    Keeps track of the total count of students, teachers, and classes.
    """

    # Class attributes to track total counts across all instances
    total_students = 0  
    total_teachers = 0  
    total_classes = 0  

    def __init__(self, school_name: str):
        """
        Constructor to initialize the school with a name.

        :param school_name: The name of the school.
        """
        self.name = school_name  # School name
        self.students = []  # List to store students enrolled in the school
        self.teachers = []  # List to store teachers in the school
        self.classes = []  # List to store classes in the school

    def add_student(self, student: Student):
        """
        Adds a student to the school and increments the total student count.

        :param student: The Student object to be added.
        """
        self.students.append(student)
        School.total_students += 1  # Update class-level student count

    def add_teacher(self, teacher: Teacher):
        """
        Adds a teacher to the school and increments the total teacher count.

        :param teacher: The Teacher object to be added.
        """
        self.teachers.append(teacher)
        School.total_teachers += 1  # Update class-level teacher count

    def add_class(self, my_class: Class):
        """
        Adds a class to the school and increments the total class count.

        :param my_class: The Class object to be added.
        """
        self.classes.append(my_class)
        School.total_classes += 1  # Update class-level class count

    def get_student_count(self) -> int:
        """
        Returns the total number of students in the school.

        :return: The total number of students.
        """
        return School.total_students

    def get_teachers_count(self) -> int:
        """
        Returns the total number of teachers in the school.

        :return: The total number of teachers.
        """
        return School.total_teachers

    def get_classes_count(self) -> int:
        """
        Returns the total number of classes in the school.

        :return: The total number of classes.
        """
        return School.total_classes
