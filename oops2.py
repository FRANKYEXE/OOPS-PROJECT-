class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        total_marks = sum(self.marks.values())
        average_marks = total_marks / len(self.marks)
        
        if any(mark < 40 for mark in self.marks.values()):
            return 'F'
        elif average_marks >= 90:
            return 'A'  
        elif average_marks >= 80:
            return 'B'
        elif average_marks >= 70:
            return 'C'
        elif average_marks >= 60:
            return 'D'
        else:
            return 'E'

    def display_summary(self):
        print(f"Student: {self.name}")
        print("Marks:", self.marks)
        print(f"Grade: {self.grade}")

if __name__ == "__main__":
    students = [
        Student("srikanta", {"Math": 95, "Science": 85, "English": 78}),
        Student("hemant", {"Math": 55, "Science": 65, "English": 72}),
        Student("preetam", {"Math": 35, "Science": 45, "English": 50}),
        Student("uday",{"Math":25,"Science":35,"English":35}),
    ]

    for student in students:
        student.display_summary()
        print()