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
               f'Средняя оценка за домашние задания: {self.average_rate()}\n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}\n'

    def average_rate(self):
        lst = []
        for value in self.grades.values():
            lst.extend(value)
        res = round(sum(lst) / len(lst), 2)
        return res

    def __eq__(self, other):  # ==
        return self.average_rate() == other.average_rate()

    def __lt__(self, other):
        return self.average_rate() < other.average_rate()

    def __le__(self, other):
        return self.average_rate() <= other.average_rate()

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

    def average_rate(self):
        lst = []
        for value in self.grades.values():
            lst.extend(value)
        res = round(sum(lst) / len(lst), 2)
        return res

    def __str__(self):
        return f'Имя: {self.atributes.get("name")}\n' \
               f'Фамилия: {self.atributes.get("surname")}\n' \
               f'Средняя оценка за лекции: {self.average_rate()}\n'

    def __eq__(self, other):  # ==
        return self.average_rate() == other.average_rate()

    def __lt__(self, other):
        return self.average_rate() < other.average_rate()

    def __le__(self, other):
        return self.average_rate() <= other.average_rate()


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


# расчет средней оценки по заданному курсу
def avg_grade_in_course(lst_student, course):
    for student in lst_student:
        if course in student.courses_in_progress:
            average_grades = round(sum(student.grades.get(course)) / len(student.grades.get(course)), 1)
            res = f'Средняя оценка по курсу {course} студента ' \
                  f'{student.atributes.get("name")} ' \
                  f'{student.atributes.get("surname")} равна {average_grades}\n'
            print(res)
    return


def compare_students(student_1, student_2):
    if isinstance(student_1, Student) and isinstance(student_2, Student):
        res = f'Средняя оценка {student_1.average_rate()} ' \
              f'студента {student_1.atributes.get("name")} {student_1.atributes.get("surname")} ' \
              f'лучше чем средняя оценка {student_2.average_rate()} у ' \
              f'студента {student_2.atributes.get("name")} {student_2.atributes.get("surname")},'
        return res


def compare_lecturer(lecturer_1, lecturer_2):
    if isinstance(lecturer_1, Lecturer) and isinstance(lecturer_2, Lecturer):
        res = f'Средняя оценка за лекции {lecturer_1.average_rate()} ' \
              f'лектора {lecturer_1.atributes.get("name")} {lecturer_1.atributes.get("surname")} ' \
              f'лучше чем средняя оценка {lecturer_2.average_rate()} у ' \
              f'лектора {lecturer_2.atributes.get("name")} {lecturer_2.atributes.get("surname")},'
        return res


lecturer_1 = Lecturer('Petra', 'Berger')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Lisa', 'Middelhauve')
lecturer_2.courses_attached += ['Git']

reviewer_1 = Reviewer('Annet', 'Olsen')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Git']

reviewer_2 = Reviewer('Manuela', 'Kraller')
reviewer_2.courses_attached += ['Java']

student_1 = Student('Ruoy', 'Eman')
student_1.finished_courses += ['Введение в программирование']
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']

student_2 = Student('Olyx', 'Ivanov')
student_2.finished_courses += ['Введение в программирование']
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']

student_1.rate_hw(lecturer_1, 'Python', 10)
student_1.rate_hw(lecturer_1, 'Python', 10)
student_1.rate_hw(lecturer_1, 'Python', 9)
student_1.rate_hw(lecturer_1, 'Python', 10)

student_2.rate_hw(lecturer_2, 'Git', 10)
student_2.rate_hw(lecturer_2, 'Git', 10)
student_2.rate_hw(lecturer_2, 'Git', 10)
student_2.rate_hw(lecturer_2, 'Git', 10)

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 10)

reviewer_1.rate_hw(student_2, 'Python', 3)
reviewer_1.rate_hw(student_2, 'Python', 4)
reviewer_1.rate_hw(student_2, 'Python', 4)
reviewer_1.rate_hw(student_2, 'Python', 5)
reviewer_1.rate_hw(student_2, 'Python', 3)

reviewer_1.rate_hw(student_2, 'Git', 4)
reviewer_1.rate_hw(student_2, 'Git', 4)
reviewer_1.rate_hw(student_2, 'Git', 4)
reviewer_1.rate_hw(student_2, 'Git', 5)

students = [student_2, student_1]
avg_grade_in_course(students, 'Python')

print(compare_students(student_1, student_2))
print(compare_lecturer(lecturer_1, lecturer_2))
print(str(student_1))
print(str(student_2))

print(str(lecturer_1))
print(str(lecturer_2))

print(str(reviewer_1))
print(str(reviewer_2))

print(lecturer_1 < lecturer_2)
print(lecturer_1 > lecturer_2)

print(lecturer_1 != lecturer_2)
print(lecturer_1 == lecturer_2)

print(lecturer_1 <= lecturer_2)
print(lecturer_1 >= lecturer_2)

print(student_1 < student_2)
print(student_1 > student_2)

print(student_1 != student_2)
print(student_1 == student_2)

print(student_1 <= student_2)
print(student_1 >= student_2)
