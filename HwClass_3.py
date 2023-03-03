class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_hw(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_attached:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'    
               
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
              
class Lecturer(Mentor, Student):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.grades = {}
    
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.grades}'
 
class Reviewer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
reviewer = Reviewer('Some', 'Buddy')
reviewer.courses_attached += ['Python']

reviewer.rate_hw(best_student, 'Python', 10)
reviewer.rate_hw(best_student, 'Python', 10)
reviewer.rate_hw(best_student, 'Python', 10)

lector = Lecturer('Oleg', 'Byligin')
lector.courses_attached += ['Python']

lector.rate_hw(lector, 'Python', 10)
lector.rate_hw(lector, 'Python', 10)
lector.rate_hw(lector, 'Python', 10)

print(best_student.grades)
print(reviewer.name, reviewer.surname, reviewer.courses_attached)
print(lector.name, lector.surname, lector.courses_attached)
print(lector.grades)
print(str(reviewer))
print()
print(str(lector))
