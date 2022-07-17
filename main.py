from class_work.Lesson_18.moduli.serice import *

name = input('Enter name: ').strip().capitalize()

def main():
    hi()
    while True:
        action = input('''
            Enter 1 to chek beautiful status
            Enter 2 to exit
            ''')
        if action == '1':
            print(f'Your beauty score is {beautiful_chek()}')
        elif action == '2':
            goodbye()
            break
        else:
            print('Incorrect action!')
if __name__ == '__main__':
    main()
