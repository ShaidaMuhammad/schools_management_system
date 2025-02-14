from abc import ABC, abstractmethod

class Person(ABC):
    """
    The base abstract class for both students and teachers.
    Defines common attributes and methods for all persons in the system.
    """

    def __init__(self, name: str, age: int):
        """
        Constructor to initialize name and age.

        :param name: The name of the person.
        :param age: The age of the person.
        """
        self._name = name  # Protected attribute for name
        self._age = age  # Protected attribute for age

    @abstractmethod
    def display_info(self):
        """
        Abstract method that must be implemented by subclasses 
        (Student and Teacher) to display personal details.
        """
        pass

    def change_name(self, new_name: str):
        """
        Changes the name of the person.

        :param new_name: The new name to be assigned.
        """
        self._name = new_name
        print("Name successfully changed to", new_name)

    def __str__(self) -> str:
        """
        Returns a string representation of the person's name.
        
        :return: The name of the person.
        """
        return self._name


class Student(Person):
    """
    Represents a student, inheriting from the Person class.
    Contains attributes and methods specific to students.
    """

    def __init__(self, name: str, age: int, student_id: str):
        """
        Constructor to initialize student details.

        :param name: The name of the student.
        :param age: The age of the student.
        :param student_id: A unique identifier for the student.
        """
        super().__init__(name, age)
        self.__student_id = student_id  # Private attribute for student ID
        self.__courses = []  # Private list to store enrolled courses

    def set_student_id(self, student_id: str):
        """
        Updates the student ID.

        :param student_id: The new student ID.
        """
        self.__student_id = student_id

    def get_student_id(self) -> str:
        """
        Retrieves the student ID.

        :return: The student ID.
        """
        return self.__student_id

    def enroll_course(self, course: str):
        """
        Enrolls the student in a course.

        :param course: The name of the course to enroll in.
        """
        if course not in self.__courses:
            self.__courses.append(course)
            print(f"{course} added to {self._name}'s courses.")
        else:
            print(f"{self._name} is already enrolled in {course}.")

    def display_courses(self):
        """
        Returns a list of courses the student is enrolled in.

        :return: List of enrolled courses or a message if none are enrolled.
        """
        return self.__courses if self.__courses else "Not enrolled in any courses."

    def display_info(self) -> str:
        """
        Displays detailed student information.

        :return: A formatted string with student details.
        """
        return f"Name: {self._name}, Age: {self._age}, ID: {self.__student_id}, Courses Enrolled: {self.__courses}"

    def __str__(self) -> str:
        """
        Returns a string representation of the student.

        :return: A formatted string with student details.
        """
        return f"Name: {self._name}, Age: {self._age}, Courses: {self.__courses}"


class Teacher(Person):
    """
    Represents a teacher, inheriting from the Person class.
    Contains attributes and methods specific to teachers.
    """

    def __init__(self, name: str, age: int, teacher_id: str, subject: str):
        """
        Constructor to initialize teacher details.

        :param name: The name of the teacher.
        :param age: The age of the teacher.
        :param teacher_id: A unique identifier for the teacher.
        :param subject: The subject the teacher specializes in.
        """
        super().__init__(name, age)
        self.__teacher_id = teacher_id  # Private attribute for teacher ID
        self.__subject = subject  # Private attribute for subject specialization

    def set_teacher_id(self, teacher_id: str):
        """
        Updates the teacher ID.

        :param teacher_id: The new teacher ID.
        """
        self.__teacher_id = teacher_id

    def get_teacher_id(self) -> str:
        """
        Retrieves the teacher ID.

        :return: The teacher ID.
        """
        return self.__teacher_id

    def assign_to_class(self, class_assigned: "Class"):
        """
        Assigns the teacher to a class.

        :param class_assigned: The class to assign the teacher to.
        """
        class_assigned.assign_teacher(self)

    def display_info(self) -> str:
        """
        Displays detailed teacher information.

        :return: A formatted string with teacher details.
        """
        return f"Name: {self._name}, Age: {self._age}, ID: {self.__teacher_id}, Subject Taught: {self.__subject}"
