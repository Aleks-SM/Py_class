[Hw classes](https://github.com/netology-code/py-homeworks-basic/tree/new_oop/6.classes)

[Методы сравнений __eq__, __ne__, __lt__, __gt__ и другие](https://proproprogs.ru/python_oop/metody-sravneniy-eq-ne-lt-gt)

Функции для подсчёта средней оценки по всем студентам и за лекции по всех лекторов можно реализовать вне классов. 

Например функцию по расчёту средней оценки за домашние задания всех студентов в рамках курса avg_grade_in_course(students, course) может принимать на себя список студентов .

Каждый студент как новый экземпляр класса Student.
best_student = Student('Kristina', 'Makarovna', 'female')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

Здесь мы добавляем оценки по каждому курсу перед подсчётом среднего балла:
best_student.rate_lector(cool_lector, 'Python', 10)
best_student.rate_lector(cool_lector, 'Python', 9)
best_student.rate_lector(cool_lector, 'Git', 9)
best_student.rate_lector(cool_lector, 'Git', 10)

Аналогично можно создать второго студента с другими оценками. Всех студентов добавляем для удобства в общий список:
students = [best_student, второй студент]

После чего функция будет примерно следующей:
def avg_grade_in_course(students, course):
    all_grades_in_course = [] # создадим пустой список
    ...здесь можно пройтись по каждому студенту из списка по конкретному курсу, взятому из аргумента функции...
    avg_grade_in_course = round(sum(all_grades_in_course) / len(all_grades_in_course), 1) #  формула расчёта среднего балла
    return avg_grade_in_course

С reviewer вся реализация будет выглядеть аналогичным образом, с той разницей, что все оценки будут адресованы уже студентам. (изменено)
