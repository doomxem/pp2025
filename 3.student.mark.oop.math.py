import math
import os

class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = {}
        self.gpa = 0
    
    def add_mark(self, course_id, mark):
        self.marks[course_id] = mark
    
    def calculate_gpa(self, courses):
        total_credits = 0
        weighted_sum = 0
        
        for course_id, mark in self.marks.items():
            if course_id in courses:
                credit = courses[course_id].credits
                total_credits += credit
                weighted_sum += mark * credit
        
        if total_credits > 0:
            self.gpa = weighted_sum / total_credits
        return self.gpa
    
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, DoB: {self.dob}, GPA: {self.gpa:.2f}"

class Course:
    def __init__(self, id, name, credits):
        self.id = id
        self.name = name
        self.credits = credits
    
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Credits: {self.credits}"

class SchoolManagement:
    def __init__(self):
        self.students = {}
        self.courses = {}
    
    def input_students(self):
        num_students = int(input("Enter number of students: "))
        for _ in range(num_students):
            print("\n--- Enter student information ---")
            id = input("Student ID: ")
            name = input("Student name: ")
            dob = input("Date of birth (DD/MM/YYYY): ")
            self.students[id] = Student(id, name, dob)
    
    def input_courses(self):
        num_courses = int(input("Enter number of courses: "))
        for _ in range(num_courses):
            print("\n--- Enter course information ---")
            id = input("Course ID: ")
            name = input("Course name: ")
            credits = int(input("Course credits: "))
            self.courses[id] = Course(id, name, credits)
    
    def input_marks(self):
        if not self.courses:
            print("No courses available. Please add courses first.")
            return
        
        if not self.students:
            print("No students available. Please add students first.")
            return
        
        print("\n--- Available Courses ---")
        for course in self.courses.values():
            print(course)
        
        course_id = input("\nEnter course ID to input marks: ")
        
        if course_id not in self.courses:
            print("Invalid course ID!")
            return
        
        print(f"\n--- Input marks for course: {self.courses[course_id].name} ---")
        for student in self.students.values():
            while True:
                try:
                    mark = float(input(f"Enter mark for {student.name} ({student.id}): "))
                    mark = math.floor(mark * 10) / 10  # Round down to 1 decimal
                    if 0 <= mark <= 20:
                        student.add_mark(course_id, mark)
                        break
                    else:
                        print("Mark must be between 0 and 20!")
                except ValueError:
                    print("Invalid input! Please enter a number.")
    
    def calculate_gpas(self):
        for student in self.students.values():
            student.calculate_gpa(self.courses)
        print("GPA calculated for all students.")
    
    def list_courses(self):
        print("\n--- List of Courses ---")
        if not self.courses:
            print("No courses available.")
        for course in self.courses.values():
            print(course)
    
    def list_students(self):
        print("\n--- List of Students ---")
        if not self.students:
            print("No students available.")
        for student in self.students.values():
            print(student)
    
    def show_student_marks(self):
        if not self.students:
            print("No students available.")
            return
        
        student_id = input("Enter student ID to view marks: ")
        if student_id not in self.students:
            print("Student not found!")
            return
        
        student = self.students[student_id]
        print(f"\n--- Marks for {student.name} ({student.id}) ---")
        
        if not student.marks:
            print("No marks available.")
            return
        
        for course_id, mark in student.marks.items():
            course_name = self.courses[course_id].name if course_id in self.courses else "Unknown Course"
            print(f"{course_name}: {mark}")
    
    def sort_students_by_gpa(self):
        if not self.students:
            print("No students available.")
            return
        
        # Calculate GPA for all students first
        for student in self.students.values():
            student.calculate_gpa(self.courses)
        
        # Sort students by GPA (descending)
        sorted_students = sorted(self.students.values(), key=lambda s: s.gpa, reverse=True)
        
        print("\n--- Students sorted by GPA (Descending) ---")
        for i, student in enumerate(sorted_students, 1):
            print(f"{i}. {student.name} - GPA: {student.gpa:.2f}")
    
    def show_menu(self):
        while True:
            print("\n" + "="*50)
            print("SCHOOL MANAGEMENT SYSTEM")
            print("="*50)
            print("1. Input students")
            print("2. Input courses")
            print("3. Input marks")
            print("4. List courses")
            print("5. List students")
            print("6. Show student marks")
            print("7. Calculate and show GPA")
            print("8. Sort students by GPA")
            print("0. Exit")
            print("-"*50)
            
            choice = input("Enter your choice (0-8): ")
            
            if choice == '1':
                self.input_students()
            elif choice == '2':
                self.input_courses()
            elif choice == '3':
                self.input_marks()
            elif choice == '4':
                self.list_courses()
            elif choice == '5':
                self.list_students()
            elif choice == '6':
                self.show_student_marks()
            elif choice == '7':
                self.calculate_gpas()
                self.list_students()
            elif choice == '8':
                self.sort_students_by_gpa()
            elif choice == '0':
                print("Goodbye!")
                break
            else:
                print("Invalid choice! Please enter 0-8.")

def main():
    # Clear screen for better UI
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("="*50)
    print("WELCOME TO STUDENT MANAGEMENT SYSTEM")
    print("="*50)
    
    school = SchoolManagement()
    school.show_menu()

if __name__ == "__main__":
    main()