class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

# Дочерний класс Lecturer (лекторы)
class Lecturer(Mentor):
    pass

# Дочерний класс Reviewer (эксперты, проверяющие ДЗ)
class Reviewer(Mentor):
    pass

# Проверка задания
lecturer = Lecturer('Иван', 'Сафонов')
reviewer = Reviewer('Пётр', 'Данилов')

print(isinstance(lecturer, Mentor))
print(isinstance(reviewer, Mentor))
print(lecturer.courses_attached)
print(reviewer.courses_attached)
