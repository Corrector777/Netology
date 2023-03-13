class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        

class Reviewer(Mentor):

    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


first_student = Student('First', 'Eman', 'man')
first_student.courses_in_progress += ['Python']
first_student.courses_in_progress += ['Java']

second_student = Student('Second', 'Eman', 'man')
second_student.courses_in_progress += ['Python']
second_student.courses_in_progress += ['C+']
second_student.courses_in_progress += ['Java']
 
first_lecturer = Lecturer('First', 'Lecturer')
first_lecturer.courses_attached += ['Python']
first_lecturer.courses_attached += ['Java']

second_lecturer = Lecturer('Second', 'Lecturer')
second_lecturer.courses_attached += ['C+']
second_lecturer.courses_attached += ['Python']

first_student.rate_lecturer(first_lecturer, 'Python', 10)
first_student.rate_lecturer(second_lecturer, 'Python', 10)
second_student.rate_lecturer(first_lecturer, 'C+', 10)
second_student.rate_lecturer(first_lecturer, 'Java', 10)
second_student.rate_lecturer(second_lecturer, 'C+', 9)

first_reviewer = Reviewer('First', ' Rewiever')
first_reviewer.courses_attached += ['Python']
first_reviewer.courses_attached += ['Java']
first_reviewer.rate_student(first_student, 'Python', 8)
first_reviewer.rate_student(second_student, 'C+', 6)
first_reviewer.rate_student(second_student, 'Git', 6)

print(f'оценки первого лектора: {first_lecturer.grades}')
print(f'оценки второго лектора: {second_lecturer.grades}')
print(f'оценки первого студента: {first_student.grades}')
print(f'оценки второго студента: {second_student.grades}')