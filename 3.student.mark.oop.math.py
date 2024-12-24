class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, id, name, credit):
        self.id = id
        self.name = name
        self.credit = credit

class Management:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def input_students(self):
        num_students = int(input("Enter number of students: "))
        for _ in range(num_students):
            id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student DOB: ")
            self.students.append(Student(id, name, dob))

    def input_courses(self):
        num_courses = int(input("Enter number of courses: "))
        for _ in range(num_courses):
            id = input("Enter course ID: ")
            name = input("Enter course name: ")
            credit = int(input("Enter course credit: "))
            self.courses.append(Course(id, name, credit))

    def input_marks(self):
        course_id = input("Enter course ID to input marks: ")
        if not any(course.id == course_id for course in self.courses):
            print("Invalid course ID!")
            return
        for student in self.students:
            mark = float(input(f"Enter mark for {student.name} (ID: {student.id}): "))
            if course_id not in self.marks:
                self.marks[course_id] = {}
            self.marks[course_id][student.id] = mark

    def list_students(self):
        print("Students:")
        for student in self.students:
            print(f"ID: {student.id}, Name: {student.name}, DOB: {student.dob}")

    def list_courses(self):
        print("Courses:")
        for course in self.courses:
            print(f"ID: {course.id}, Name: {course.name}, Credit: {course.credit}")

    def show_marks(self):
        course_id = input("Enter course ID to view marks: ")
        if course_id not in self.marks:
            print("No marks found for this course.")
            return
        print("Marks:")
        for student in self.students:
            mark = self.marks[course_id].get(student.id, "N/A")
            print(f"{student.name} (ID: {student.id}): {mark}")

    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Input students")
            print("2. Input courses")
            print("3. Input marks")
            print("4. List students")
            print("5. List courses")
            print("6. Show marks")
            print("7. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.input_students()
            elif choice == "2":
                self.input_courses()
            elif choice == "3":
                self.input_marks()
            elif choice == "4":
                self.list_students()
            elif choice == "5":
                self.list_courses()
            elif choice == "6":
                self.show_marks()
            elif choice == "7":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if _name_ == "_main_":
    management = Management()
    management.menu()