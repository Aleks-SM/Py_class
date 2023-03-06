class Human:
    def __init__(self, name, surname):
        self.atributes = {'name': name, 'surname': surname}

    def average_rate(self):
        lst = []
        for value in self.grades.values():
            lst.extend(value)
        return '{:.3}'.format(sum(lst) / len(lst))
    
    def __eq__(self, other):  # ==
        return average_rate(self) == average_rate(other)

    def __lt__(self, other):
        return average_rate(self) < average_rate(other)

    def __le__(self, other):
        return average_rate(self) <= average_rate(other)
  
class Student(Human):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.atributes.get("name")}\n' \
               f'Фамилия: {self.atributes.get("surname")}\n' \
               f'Средняя оценка за домашние задания: {self.average_rate()}\n' \
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
               f'Средняя оценка за лекции: {self.average_rate()}\n'

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

student1 = Student('Ruoy', 'Eman')
student1.finished_courses += ['Введение в программирование']
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Git']

student2 = Student('Olyx', 'Ivanov')
student2.finished_courses += ['Введение в программирование']
student2.courses_in_progress += ['Python']
student2.courses_in_progress += ['Java']

student1.rate_hw(lecturer1, 'Python', 10)
student1.rate_hw(lecturer1, 'Python', 10)
student1.rate_hw(lecturer1, 'Python', 9)
student1.rate_hw(lecturer1, 'Python', 10)

student2.rate_hw(lecturer2, 'Git', 10)
student2.rate_hw(lecturer2, 'Git', 9)
student2.rate_hw(lecturer2, 'Git', 9)
student2.rate_hw(lecturer2, 'Git', 10)

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 10)

reviewer1.rate_hw(student2, 'Python', 3)
reviewer1.rate_hw(student2, 'Python', 4)
reviewer1.rate_hw(student2, 'Python', 4)
reviewer1.rate_hw(student2, 'Python', 5)

print(str(student1))
print(str(student2))

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

print(student1 < student2)
print(student1 > student2)

print(student1 != student2)
print(student1 == student2)

print(student1 <= student2)
print(student1 >= student2)
