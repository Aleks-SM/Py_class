class Human:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class Student(Human):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_rate()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}\n'

    def average_rate(self):
        lst = []
        for value in self.grades.values():
            lst.extend(value)
        return '{:.3}'.format(sum(lst) / len(lst))

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def add_courses_in_progress(self, course_name):
        self.courses_in_progress.append(course_name)

class Mentor(Human):
    def __init__(self, name, surname):
        super().__init__(name, surname, )
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname, )
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rate()}\n'

    def average_rate(self):
        lst = []
        for value in self.grades.values():
            lst.extend(value)
        return '{:.3}'.format(sum(lst) / len(lst))

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname, )

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nЧитает лекции на курсах: {", ".join(self.courses_attached)}\n'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

lecturer = Lecturer('Petra', 'Berger')
lecturer.courses_attached += ['Python']

reviewer = Reviewer('Annet', 'Olsen')
reviewer.courses_attached += ['Python']

best_student = Student('Ruoy', 'Eman')
best_student.finished_courses += ['Введение в программирование']
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']

bad_student = Student('Olyx', 'Ivanov')
bad_student.finished_courses += ['Введение в программирование']
bad_student.courses_in_progress += ['Python']
bad_student.courses_in_progress += ['Java']

best_student.rate_hw(lecturer, 'Python', 10)
best_student.rate_hw(lecturer, 'Python', 10)
best_student.rate_hw(lecturer, 'Python', 9)
best_student.rate_hw(lecturer, 'Python', 10)

reviewer.rate_hw(best_student, 'Python', 10)
reviewer.rate_hw(best_student, 'Python', 9)
reviewer.rate_hw(best_student, 'Python', 9)
reviewer.rate_hw(best_student, 'Python', 10)

reviewer.rate_hw(bad_student, 'Python', 3)
reviewer.rate_hw(bad_student, 'Python', 4)
reviewer.rate_hw(bad_student, 'Python', 4)
reviewer.rate_hw(bad_student, 'Python', 5)

print(str(best_student))
print(str(bad_student))

print(str(lecturer))

print(str(reviewer))

lecturer = Lecturer('Lisa', 'Middelhauve')
lecturer.courses_attached += ['Git']

best_student.rate_hw(lecturer, 'Git', 10)
best_student.rate_hw(lecturer, 'Git', 10)
best_student.rate_hw(lecturer, 'Git', 9)
best_student.rate_hw(lecturer, 'Git', 10)
print(str(lecturer))

reviewer = Reviewer('Manuela', 'Kraller')
reviewer.courses_attached += ['Java']
print(str(reviewer))