class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
     
    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def average_grades(self):
        for list_grades in self.grades.values():
            if list_grades: 
                return sum(list_grades) / len(list_grades)
            return 0 
    
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.average_grades()} \nКурсы в процессе изучения: {', '.join(self.courses_in_progress)} \nЗавершенные курсы: {', '.join(self.finished_courses)}'

    def __lt__(self, value):
        return self.average_grades() < value.average_grades()
   
    def __eq__(self, value):
        return self.average_grades() == value.average_grades()

    def __gt__(self, value):
        return self.average_grades() > value.average_grades()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        

class  Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def average_grades(self):
        for list_grades in self.grades.values():
            if list_grades: 
                return sum(list_grades) / len(list_grades)
            return 0 
    
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_grades()}'

    def __lt__(self, value):
        return self.average_grades() < value.average_grades()
   
    def __eq__(self, value):
        return self.average_grades() == value.average_grades()

    def __gt__(self, value):
        return self.average_grades() > value.average_grades()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'



student_1 = Student('Bob', 'Parker', 'male')
student_2 = Student('Erika', 'Brown', 'female')

lecturer_1 = Lecturer('Arhas', 'Chal')
lecturer_2 = Lecturer('Vitor', 'Jonson')

reviewer_1 = Reviewer('Nick', 'Rofl')
reviewer_2 = Reviewer('Sirius', 'Black')



student_1.courses_in_progress += ['Python', 'Git']
student_2.courses_in_progress += ['Python']
student_1.finished_courses += ['Основы в программировании']
student_2.finished_courses += ['GO', 'C++']

lecturer_1.courses_attached += ['Python']
lecturer_2.courses_attached += ['Java']

reviewer_1.courses_attached += ['Python', 'Git']
reviewer_2.courses_attached += ['Python']

student_1.rate_lecture(lecturer_1, 'Python', 9)
student_1.rate_lecture(lecturer_1, 'Python', 7)
student_2.rate_lecture(lecturer_2, 'Java', 10)
student_2.rate_lecture(lecturer_2, 'Java', 6)

reviewer_1.rate_hw(student_1, 'Python', 7)
reviewer_1.rate_hw(student_1, 'Python', 5)
reviewer_2.rate_hw(student_2, 'Java', 3)
reviewer_2.rate_hw(student_2, 'Java', 6)

print(lecturer_1 > student_1)
print(lecturer_2 < student_2)
print(lecturer_1 == lecturer_2)

print(student_1)
print(reviewer_1)
print(lecturer_1)



def average_hw_grade(students, course):
    grades = []
    for student in students:
        if course in student.grades:
            grades.extend(student.grades[course])
    if grades:
        return sum(grades) / len(grades)
    return 0

def average_lecturers_grade(lecturers, course):
    grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            grades.extend(lecturer.grades[course])
    if grades:
        return sum(grades) / len(grades)
    return 0





 
