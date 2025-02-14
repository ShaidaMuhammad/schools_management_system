from school import School
from person import Student, Teacher
from class_ import Class

# Create a school instance
icp = School("Islamia College Peshawar")

# Create a class and add it to the school
class_10 = Class("10th")
icp.add_class(class_10)

# Create student instances
student_1 = Student("Ali", 18, "S001")
student_2 = Student("Khan", 30, "S002")

# Add students to the school
icp.add_student(student_1)
icp.add_student(student_2)

# Enroll students in courses
student_1.enroll_course("Mathematics")
student_1.enroll_course("Computer Science")
student_2.enroll_course("Mathematics")
student_2.enroll_course("Physics")

# Create teacher instances
teacher_1 = Teacher("Muhammad", 40, "T001", "Physics")
teacher_2 = Teacher("Umar", 45, "T002", "Mathematics")
teacher_3 = Teacher("Usman", 35, "T003", "Computer Science")

# Add teachers to the school
icp.add_teacher(teacher_1)
icp.add_teacher(teacher_2)
icp.add_teacher(teacher_3)

# Add students to the class
class_10.add_student(student_1)
class_10.add_student(student_2)

# Assign teachers to the class
class_10.assign_teacher(teacher_1)
class_10.assign_teacher(teacher_2)
class_10.assign_teacher(teacher_3)

# Display student and teacher information
print(student_1.display_info())
print(teacher_1.display_info())

# Display total counts of classes, students, and teachers in the school
print("Total Count of Classes:", icp.get_classes_count())
print("Total Count of Students:", icp.get_student_count())
print("Total Count of Teachers:", icp.get_teachers_count())
