from person import Student, Teacher

class Class:
    """
    Represents a school class that can have multiple students and teachers.
    This class manages student enrollment and teacher assignments.
    """

    def __init__(self, class_name: str):
        """
        Constructor to initialize a class with a name.

        :param class_name: The name of the class (e.g., "10th Grade").
        """
        self.__class_name = class_name  # Private attribute to store class name
        self.__students_enrolled = []  # Private list to store enrolled students
        self.__teachers_assigned = []  # Private list to store assigned teachers

    def add_student(self, student: Student):
        """
        Adds a student to the class if not already enrolled.

        :param student: The Student object to be added.
        """
        if student not in self.__students_enrolled:
            self.__students_enrolled.append(student)
            print("Student added successfully:", student)
        else:
            print("Student already enrolled:", student)

    def assign_teacher(self, teacher: Teacher):
        """
        Assigns a teacher to the class if not already assigned.

        :param teacher: The Teacher object to be assigned.
        """
        if teacher not in self.__teachers_assigned:
            self.__teachers_assigned.append(teacher)
            print("Teacher assigned successfully:", teacher)
        else:
            print("Teacher already assigned:", teacher)

    def __str__(self) -> str:
        """
        Returns a formatted string representing the class details.

        :return: A string listing the class name, enrolled students, and assigned teachers.
        """
        return (f"Class Name: {self.__class_name}, Students Enrolled: {[student._name for student in self.__students_enrolled]}, Teachers Assigned: {[teacher._name for teacher in self.__teachers_assigned]}")
