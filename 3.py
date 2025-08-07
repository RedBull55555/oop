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
            lecturer.grades.setdefault(course, []).append(grade)
        else:
            return 'Ошибка'

    def average_grade(self):
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __str__(self):
        avg = self.average_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished = ', '.join(self.finished_courses)
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {avg:.1f}\n'
                f'Курсы в процессе изучения: {courses_in_progress}\n'
                f'Завершенные курсы: {finished}')

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() == other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __str__(self):
        avg = self.average_grade()
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {avg:.1f}')

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() == other.average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            student.grades.setdefault(course, []).append(grade)
        else:
            return 'Ошибка'

    def __str__(self):
        return super().__str__()



#Проверка
student1 = Student('Ольга', 'Алёхина', 'Ж')
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Введение в программирование']
student1.grades = {'Python': [9, 10], 'Git': [8]}

student2 = Student('Иван', 'Смирнов', 'М')
student2.courses_in_progress += ['Python']
student2.grades = {'Python': [5, 7, 6]}

lecturer1 = Lecturer('Иван', 'Иванов')
lecturer1.courses_attached += ['Python']
lecturer1.grades = {'Python': [10, 9]}

lecturer2 = Lecturer('Павел', 'Петров')
lecturer2.courses_attached += ['Python']
lecturer2.grades = {'Python': [8, 9]}

reviewer = Reviewer('Анна', 'Сидорова')
reviewer.courses_attached += ['Python']

print(student1)
print()
print(lecturer1)
print()
print(reviewer)
print()
print(student1 > student2)    # True
print(lecturer1 > lecturer2)  # True
