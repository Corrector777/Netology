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
        if (isinstance(lecturer, Lecturer) and course in
            lecturer.courses_attached and course in self.courses_in_progress
            and 1 <= grade <= 10):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def score_count(self):
        if not self.grades:
            return 0
        sum_of_rates = sum(map(sum, self.grades.values()))
        lections_count = sum(map(len, self.grades.values()))
        return sum_of_rates/lections_count
        # sum_of_rates = 0
        # lections_count = 0
        # for key, value in stats.items():
        #     sum_of_rates += sum(stats[key])
        #     lections_count += len(value)
        # return sum_of_rates/lections_count  

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия:{self.surname}\n'
                f'Средний бал за д.з.: {self.score_count(): .1f}\n'
                f'Курсы в процессе: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы:{", ".join(self.finished_courses)}')
    
    @classmethod
    def varify(cls, other):
        if not isinstance(other, Student):
            raise Exception(' Ошибка сравнения. Разные классы')
        return other.score_count()

    def __lt__(self, other):
        return self.score_count() < self.varify(other)
        
    def __le__(self, other):
        return self.score_count() <= self.varify(other)
        
    def __eq__(self, other):
        return self.score_count() == self.varify(other)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.avarange_score = float

    def score_count(self):
        if not self.grades:
            return 0
        sum_of_rates = sum(map(sum, self.grades.values()))
        lections_count = sum(map(len, self.grades.values()))
        # self.avarange_score = sum_of_rates/lections_count
        return sum_of_rates/lections_count
    
    @classmethod
    def varify(cls, other):
        if not isinstance(other, Lecturer):
            raise TypeError(' Ошибка сравнения. Разные классы')
        return other.score_count()

    def __lt__(self, other):
        return self.score_count() < self.varify(other)
        
    def __le__(self, other):
        return self.score_count() <= self.varify(other)
        
    def __eq__(self, other):
        return self.score_count() == self.varify(other)
      
    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия:{self.surname}\n'
                f'Средний бал за лекции: {self.score_count(): .1f}\n')


class Reviewer(Mentor):
    def rate_student(self, student, course, grade):
        if (isinstance(student, Student)
            and course in student.courses_in_progress
            and 1 <= grade <= 10):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия:{self.surname}\n')    


first_student = Student('First', 'Eman', 'man')
first_student.courses_in_progress += ['Python']
first_student.courses_in_progress += ['Pascal']
first_student.courses_in_progress += ['Java']
first_student.courses_in_progress += ['C+']
first_student.add_courses('Git')

second_student = Student('Second', 'Eman', 'man')
second_student.courses_in_progress += ['Python']
second_student.courses_in_progress += ['C+']
second_student.courses_in_progress += ['Java']

third_student = Student('Third', 'Eman', 'woman')
third_student.courses_in_progress += ['Python']
third_student.courses_in_progress += ['C+']
third_student.courses_in_progress += ['Java']

first_lecturer = Lecturer('First', 'Lecturer')
first_lecturer.courses_attached += ['Python']
first_lecturer.courses_attached += ['Java']
first_lecturer.courses_attached += ['C+']

second_lecturer = Lecturer('Second', 'Lecturer')
second_lecturer.courses_attached += ['C+']
second_lecturer.courses_attached += ['Python']
second_lecturer.courses_attached += ['Pascal']
second_lecturer.courses_attached += ['Java']

first_student.rate_lecturer(first_lecturer, 'Python', 3)
first_student.rate_lecturer(second_lecturer, 'Python', 5)
first_student.rate_lecturer(second_lecturer, 'Pascal', 4)
second_student.rate_lecturer(first_lecturer, 'C+', 8)
second_student.rate_lecturer(first_lecturer, 'Java', 7)
third_student.rate_lecturer(first_lecturer, 'Java', 7)
third_student.rate_lecturer(second_lecturer, 'Pascal', 4)

first_reviewer = Reviewer('First', ' Rewiever')
second_reviewer = Reviewer('Second', ' Rewiever')
# first_reviewer.rate_student(first_student, 'Python', 4)
# first_reviewer.rate_student(first_student, 'Python', 10)
# first_reviewer.rate_student(first_student, 'Pascal', 6)
# first_reviewer.rate_student(second_student, 'C+', 6)
# first_reviewer.rate_student(first_student, 'C+', 6)
first_reviewer.rate_student(second_student, 'Java', 10)
first_reviewer.rate_student(second_student, 'Python', 10)
first_reviewer.rate_student(third_student, 'C+', 6)
first_reviewer.rate_student(third_student, 'C+', 6)

print('\nСтуденты:\n')
print(first_student, '\n')
print(second_student, '\n')
print(third_student)

print('\nЛекторы:\n')
print(first_lecturer, '\n')
print(second_lecturer)

print('\nРевьюверы:\n')
print(first_reviewer, '\n')
print(second_reviewer)

# print(first_student.avarange_score)
# print(second_student.avarange_score)
print('\n\n<-сравнение среднего балла->\n\n')
print(first_student <= second_student)
print(first_lecturer >= second_lecturer)
print(first_student >= third_student)

# print(first_student.grades)
# print(second_student.grades)

print('\n\n<-проверка функций->\n\n')

students_list = [first_student, second_student, third_student]


def students_avarange_score(students_list, course):
    course_participant = []
    all_score = 0
    counter = 0
    for student in students_list:
        if course in student.grades:
            counter += 1
            course_participant.append(student.name)
            all_score += sum(student.grades[course])
    if counter == 0:
        return f'{course}: нет оценок курса'
    else:
        return (f'Средний балл среди студентов по курсу {course} равен: '
                f'{all_score/counter: .1f}--> общий балл по курсу: {all_score}, '
                f' \nвсего студентов, получивших оценки на курсе: {counter} ({", ".join(course_participant)})\n')


lecturers_list = [first_lecturer, second_lecturer]


def lecturers_avarange_score(lecturers_list, course):
    course_participant = []
    all_score = 0
    counter = 0
    for lector in lecturers_list:
        if course in lector.grades:
            counter += 1
            course_participant.append(lector.name)
            all_score += sum(lector.grades[course])
    if counter == 0:
        return (f'{course}: нет оценок курса')
    else:                        
        return (f'Средний балл среди лекторов по курсу {course} равен: '
                f'{all_score/counter: .1f}--> общий балл по курсу: {all_score},'
                f' \nвсего лекторов, получивших оценки на курсе: {counter} ({", ".join(course_participant)})\n')


print(students_avarange_score(students_list, 'C+'))
print(students_avarange_score(students_list, 'Java'))

print(lecturers_avarange_score(lecturers_list, 'Python'))
print(lecturers_avarange_score(lecturers_list, 'C+'))
print(lecturers_avarange_score(lecturers_list, 'Pascal'))
print(lecturers_avarange_score(lecturers_list, 'ЛЛ'))
print(Reviewer.mro())