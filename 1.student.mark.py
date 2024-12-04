students = []
courses = []
marks = {}
def input_Students():
    NumberOfStudentInClass = input("Enter the number of all students in class: ")
    for i in range(NumberOfStudentInClass):
        StudentID = input("Student ID: ")
        StudentName = input("Student Name: ")
        StudentBirthday = input("Student Birthday: ")
        Students.append(("StudentID", "StudentName", "StudentBirthday"))
def input_Courses():
    NumberOfCourses = input("Enter the number of Courses:")
    for i in range(NumberOfCourses):
        CoursesID = input("Courses ID: ")
        CoursesName = input("Courses Name: ")
        Courses.append(("CoursesID", "CoursesName"))
def input_Marks():
    CoursesID = input("Courses ID to get mark: ")
    for course in courses:
        if CoursesID == course[0]:
            break
        else:
            print("Course not found.")
    return
    course_marks = dict()
    for student in students:
        mark = input(f"Enter marks for {student[1]} (ID: {student[0]}): ")
        course_marks[student[0]] = mark
    marks[CoursesID] = course_marks
def listCourses():
    print("Courses:")
    for course in courses:
        print(f"ID: {course[0]}, Name: {course[1]}")
def listStudents():
    print("Students:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, DoB: {student[2]}")
def showMarks():
    CoursesID = input("Enter course ID to show marks: ")
    if CoursesID not in marks:
        print("No marks found for this course.")
        return  
    print("Marks for course:", CoursesID)
    for CoursesID, mark in marks[CoursesID].items():
        for student in students:
            if student[0] == CoursesID:
                StudentName = student[1]
                break  
        print("Student:", StudentName, ", ID:", CoursesID, ", Mark:", mark)


def main():
    while True:
        print("\nStudent Mark Management System")
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks")
        print("4. List courses")
        print("5. List students")
        print("6. Show marks")
        print("7. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            Students()
        elif choice == "2":
            Courses()
        elif choice == "3":
            Marks()
        elif choice == "4":
            listCourses()
        elif choice == "5":
            listStudents()
        elif choice == "6":
            showMarks()
        elif choice == "7":
            print(":<")
            break
        else:
            print("Invalid choice. Please try again.")