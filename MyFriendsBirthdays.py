# /home/pol/.config/birthdays/MyBirthdays.data
import os
import sys
import datetime


def month_from_num(number):
    month_dict = {1: 'январь', 2: 'февраль', 3: 'март', 4: 'апрель', 5: 'май',
                  6: 'июнь', 7: 'июль', 8: 'август', 9: 'сентябрь',
                  10: 'октябрь',
                  11: 'ноябрь', 12: 'декабрь'
                  }
    return month_dict.get(number, 'Неизвестный месяц')


def load_data_from_file(file, arr_list):
    if not (os.path.isfile(file)):
        print('Файл: {} не найден!'.format(file))

    user_arr_data = []
    infile = open(file, 'r', encoding='utf-8')
    for line in infile:
        temp = line.strip()
        if temp.startswith('#') or temp == '':
            continue
        else:
            arr = list(map(str.strip, temp.split('\t')))
            if len(arr) != 3:
                print(arr)
                print('Данные повреждены!\n'
                      'Записи должны разделяться символом табуляции!')
                sys.exit()
            user_arr_data.append(arr[:])
    infile.close()
    my_dict = {}
    for i in user_arr_data:
        my_dict['nickname'] = i[0]
        my_dict['name'] = i[2]
        my_dict['day'] = int(i[1][0:2])
        my_dict['month'] = int(i[1][3:5])
        my_dict['year'] = int(i[1][-4:])
        my_dict['birthday'] = i[1]
        arr_list.append(my_dict.copy())
        my_dict.clear()


def is_chek_data(data_list):
    if len(data_list) <= 0:
        return False
    return True


def get_next_month(current_month):
    if 1 <= current_month <= 11:
        return current_month + 1
    return 1


def get_prev_month(current_month):
    if 2 <= current_month <= 12:
        return current_month - 1
    return 12


def select_case_birthdays(current_day, current_month, current_year, user_arr):
    prev_month = get_prev_month(current_month)
    next_month = get_next_month(current_month)
    prev_month_data = []
    next_month_data = []
    current_month_data = []

    for i in range(len(user_arr)):
        if user_arr[i]['month'] == prev_month:
            prev_month_data.append(user_arr[i])
        elif user_arr[i]['month'] == next_month:
            next_month_data.append(user_arr[i])
        elif user_arr[i]['month'] == current_month:
            current_month_data.append(user_arr[i])

    print_birthdays_month(current_day, current_month, current_year,
                          prev_month_data, 'prev')

    print_birthdays_month(current_day, current_month, current_year,
                          current_month_data, 'current')

    print_birthdays_month(current_day, current_month, current_year,
                          next_month_data, 'next')


#
def print_birthdays_month(current_day, current_month, current_year,
                          user_arr, flag):
    print()
    for i in range(len(user_arr)):
        if flag == 'prev':
            word = 'Ранее'
            age = current_year - user_arr[i]['year']
            if current_month == 1:
                age -= 1
        elif flag == 'next':
            word = 'Далее'
            age = current_year - user_arr[i]['year']  #- 1
            if current_month == 12:
                age += 1
        elif flag == 'current':
            if user_arr[i]['day'] < current_day:
                age = current_year - user_arr[i]['year']
                word = 'Чуть ранее'
            elif user_arr[i]['day'] == current_day:
                age = current_year - user_arr[i]['year']
                word = 'Сегодня!'
            elif user_arr[i]['day'] > current_day:
                age = current_year - user_arr[i]['year'] #- 1
                word = 'Совсем скоро'
            else:
                word = 'Сейчас'
                age = 0
        else:
            word = ''
            age = 0
        # print(f'{word}: nickname: {user_arr[i]["nickname"]},
        # имя: {user_arr[i]["name"]}, возраст: {age},
        # дата рождения: {user_arr[i]["birthday"]}')
        nick = user_arr[i]["nickname"] + ', '
        if nick == '-, ':
            nick = ''
        else:
            nick = ' ' + nick
        print(f'{word}:{nick} {user_arr[i]["name"]}, {age},'
              f' {user_arr[i]["birthday"]}')


if sys.platform[0:6] != 'linux':
    print('This program for Linux only!')
    sys.exit()

if sys.version_info[0] < 3:
    print('This program for Python version >= 3 !')
    sys.exit()

userHome = os.path.expanduser('~')
userName = os.path.split(userHome)[-1]
userDataFile = '/home/' + userName + '/.config/birthdays/MyBirthdays.data'

userArrDictData = []

load_data_from_file(userDataFile, userArrDictData)

if is_chek_data(userArrDictData):
    print('Загружено {} записей.'.format(len(userArrDictData)))
else:
    print('Данные не загружены! Программа завершает работу')
    sys.exit()

nowDate = datetime.datetime.now()
nowDateDay, nowDateMonth = nowDate.day, nowDate.month
nowDateYear = nowDate.year
#  #nowDateDay, nowDateMonth, nowDateYear = 2,1,2022
print(f'Сегодня: {nowDateDay} {month_from_num(nowDateMonth)} '
      f'{nowDateYear} год')

select_case_birthdays(nowDateDay, nowDateMonth, nowDateYear, userArrDictData)
