# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

name_count = {}
for student in students:
    name = student['first_name']
    if name in name_count:
        name_count[name] += 1
    else:
        name_count[name] = 1

for name, count in name_count.items():
    print(f"{name}: {count}")


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
name_count = {}
for student in students:
    name = student['first_name']
    if name in name_count:
        name_count[name] += 1
    else:
        name_count[name] = 1
max_name = max(name_count, key=name_count.get)
print(f"Самое частое имя среди учеников: {max_name}")

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
class_number=1
for groups in school_students:
    name_count={}
    group=groups
    for student in group:
        name = student['first_name']
        if name in name_count:
            name_count[name] += 1
        else:
            name_count[name] = 1
    max_name = max(name_count, key=name_count.get)
    print(f"самое частое имя в классе {class_number}: {max_name}")
    class_number+=1

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

for groups in school:
    man_cnt=0
    woman_cnt=0
    for student in groups['students']:
        for name in student.values():
            if is_male[name]:
                man_cnt += 1
            else:
                woman_cnt += 1    
    print(f"Класс {groups['class']}: девочки {woman_cnt}, мальчики {man_cnt}" )


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
most_boys_class = ''
most_girls_class = ''
max_men = 0
max_women = 0

for groups in school:
    man_cnt=0
    woman_cnt=0
    class_name=groups['class']
    for student in groups['students']:
        name = student['first_name']
        if is_male[name]:
            man_cnt += 1
        else:
            woman_cnt += 1
    if man_cnt > max_men:
        max_men=man_cnt
        most_boys_class=class_name
    if woman_cnt > max_women:
        max_women = woman_cnt
        most_girls_class = class_name    
    
print(f"Больше всего мальчиков в классе {most_boys_class}")
print(f"Больше всего девочек в классе {most_girls_class}")

