from class_work.Lesson_18.moduli.validate import validate_data

name = input('Enter name: ').strip().capitalize()


def hi():
    print(f'Hi {name}!')
    return name


def goodbye():
    print(f'Goodbye {name}')


def beautiful_chek():
    cd = validate_data()
    li = (cd[0] * cd[1] * cd[2]) / ((cd[3] ** 2) * cd[4])
    return li
