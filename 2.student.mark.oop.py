class Student:
    def __init__(self, stu_id, name, dob):
        self.__stu_id = stu_id
        self.__name = name
        self.__dob = dob

    def get_id(self):
        return self.__stu_id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def __str__(self):
        return f"ID: {self.__stu_id}, Name: {self.__name}, DoB: {self.__dob}"


class Course:
    def __init__(self, course_id, name):
        self.__course_id = course_id
        self.__name = name

    def get_id(self):
        return self.__course_id

    def get_name(self):
        return self.__name

    def __str__(self):
        return f"Course ID: {self.__course_id}, Name: {self.__name}"


class Mark:
    def __init__(self, student, course, mark):
        self.__student = student
        self.__course = course
        self.__mark = mark

    def get_student_id(self):
        return self.__student.get_id()

    def get_course_id(self):
        return self.__course.get_id()

    def get_mark(self):
        return self.__mark

    def __str__(self):
        return f"Student: {self.__student.get_name()} ({self.__student.get_id()}) - Mark: {self.__mark}"


class StudentMarkSystem:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks = []

    # Input methods with encapsulation
    def input_student_num(self):
        try:
            n = int(input("Input number of students: "))
            for _ in range(n):
                self.__input_student_info()
        except ValueError:
            print("Invalid input! Please enter a number.")

    def __input_student_info(self):
        stu_id = input("Student ID: ")
        name = input("Student Name: ")
        dob = input("Date of birth: ")
        self.__students.append(Student(stu_id, name, dob))

    def input_course_num(self):
        try:
            n = int(input("Input number of courses: "))
            for _ in range(n):
                self.__input_course_info()
        except ValueError:
            print("Invalid input! Please enter a number.")

    def __input_course_info(self):
        course_id = input("Course ID: ")
        name = input("Course Name: ")
        self.__courses.append(Course(course_id, name))

    def input_mark(self):
        course_id = input("Input Course ID to enter marks: ")
        course = self.__find_course_by_id(course_id)
        if not course:
            print("Course ID not found.")
            return
        
        for student in self.__students:
            try:
                m = float(input(f"Input mark for {student.get_name()} (ID: {student.get_id()}): "))
                if m < 0:
                    print("Invalid mark! Mark cannot be negative.")
                    return
                self.__marks.append(Mark(student, course, m))
            except ValueError:
                print("Invalid input! Please enter a number.")
                return

    # Listing methods
    def list_courses(self):
        if not self.__courses:
            print("No courses available.")
            return
        print("\n=== List of Courses ===")
        for course in self.__courses:
            print(course)

    def list_students(self):
        if not self.__students:
            print("No students available.")
            return
        print("\n=== List of Students ===")
        for student in self.__students:
            print(student)

    def show_mark(self):
        course_id = input("Input Course ID to show marks: ")
        course = self.__find_course_by_id(course_id)
        if not course:
            print("Course ID not found.")
            return
        
        print(f"\n=== Marks for {course.get_name()} ===")
        found = False
        for mark in self.__marks:
            if mark.get_course_id() == course_id:
                print(mark)
                found = True
        
        if not found:
            print("No marks available for this course.")

    # Helper method (private)
    def __find_course_by_id(self, course_id):
        for course in self.__courses:
            if course.get_id() == course_id:
                return course
        return None

    # Main menu
    def run(self):
        while True:
            print("\n" + "="*40)
            print("STUDENT MARK MANAGEMENT SYSTEM")
            print("="*40)
            print("1. Input number of students")
            print("2. Input number of courses")
            print("3. Input marks for a course")
            print("4. List all courses")
            print("5. List all students")
            print("6. Show marks for a course")
            print("7. Exit")
            print("="*40)
            
            choice = input("Choose: ")
            
            if choice == '1':
                self.input_student_num()
            elif choice == '2':
                self.input_course_num()
            elif choice == '3':
                self.input_mark()
            elif choice == '4':
                self.list_courses()
            elif choice == '5':
                self.list_students()
            elif choice == '6':
                self.show_mark()
            elif choice == '7':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    system = StudentMarkSystem()
    system.run()