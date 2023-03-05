from pprint import pprint


class Human:
    def __init__(self, name, surname):
        self.atributes = {'name': name, 'surname': surname}


class Student(Human):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.atributes.get("name")}\n' \
               f'Фамилия: {self.atributes.get("surname")}\n' \
               f'Средняя оценка за домашние задания: {average_rate(self)}\n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}\n'

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

    def __eq__(self, other):  # ==
        return average_rate(self) == average_rate(other)

    def __lt__(self, other):
        return average_rate(self) < average_rate(other)

    def __le__(self, other):
        return average_rate(self) <= average_rate(other)


class Mentor(Human):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.atributes.get("name")}\n' \
               f'Фамилия: {self.atributes.get("surname")}\n' \
               f'Средняя оценка за лекции: {average_rate(self)}\n'

    def __eq__(self, other):  # ==
        return average_rate(self) == average_rate(other)

    def __lt__(self, other):
        return average_rate(self) < average_rate(other)

    def __le__(self, other):
        return average_rate(self) <= average_rate(other)


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.atributes.get("name")}\n' \
               f'Фамилия: {self.atributes.get("surname")}\n' \
               f'Читает лекции на курсах: {", ".join(self.courses_attached)}\n'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def average_rate(person):
    lst = []
    for value in person.grades.values():
        lst.extend(value)
    return '{:.3}'.format(sum(lst) / len(lst))


lecturer1 = Lecturer('Petra', 'Berger')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Lisa', 'Middelhauve')
lecturer2.courses_attached += ['Git']

reviewer1 = Reviewer('Annet', 'Olsen')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Manuela', 'Kraller')
reviewer2.courses_attached += ['Java']

best_student = Student('Ruoy', 'Eman')
best_student.finished_courses += ['Введение в программирование']
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']

bad_student = Student('Olyx', 'Ivanov')
bad_student.finished_courses += ['Введение в программирование']
bad_student.courses_in_progress += ['Python']
bad_student.courses_in_progress += ['Java']

best_student.rate_hw(lecturer1, 'Python', 10)
best_student.rate_hw(lecturer1, 'Python', 10)
best_student.rate_hw(lecturer1, 'Python', 9)
best_student.rate_hw(lecturer1, 'Python', 10)

bad_student.rate_hw(lecturer2, 'Git', 10)
bad_student.rate_hw(lecturer2, 'Git', 9)
bad_student.rate_hw(lecturer2, 'Git', 9)
bad_student.rate_hw(lecturer2, 'Git', 10)

reviewer1.rate_hw(best_student, 'Python', 10)
reviewer1.rate_hw(best_student, 'Python', 9)
reviewer1.rate_hw(best_student, 'Python', 9)
reviewer1.rate_hw(best_student, 'Python', 10)

reviewer1.rate_hw(bad_student, 'Python', 3)
reviewer1.rate_hw(bad_student, 'Python', 4)
reviewer1.rate_hw(bad_student, 'Python', 4)
reviewer1.rate_hw(bad_student, 'Python', 5)

print(str(best_student))
print(str(bad_student))

print(str(lecturer1))
print(str(lecturer2))

print(str(reviewer1))
print(str(reviewer2))

print(lecturer1 < lecturer2)
print(lecturer1 > lecturer2)

print(lecturer1 != lecturer2)
print(lecturer1 == lecturer2)

print(lecturer1 <= lecturer2)
print(lecturer1 >= lecturer2)

print(best_student < bad_student)
print(best_student > bad_student)

print(best_student != bad_student)
print(best_student == bad_student)

print(best_student <= bad_student)
print(best_student >= bad_student)