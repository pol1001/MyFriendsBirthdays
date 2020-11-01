# /home/pol/.config/birthdays/MyBirthdays.data
import os
import sys
import datetime


def load_data_from_file(file, arr_list):
    if not (os.path.isfile(file)):
        print('Файл: {} не найден!'.format(file))
        return None
    userarrdata = []
    infile = open(file, 'r', encoding='utf-8')
    for line in infile:
        temp = line.strip()
        if temp.startswith('#'):
            continue
        else:
            arr = list(map(lambda x: x.strip(), temp.split('\t')))
            userarrdata.append(arr[:])
    infile.close()
    my_dict = {}
    for i in userarrdata:
        my_dict['nickname'] = i[0]
        my_dict['name'] = i[2]
        my_dict['day'] = int(i[1][0:2])
        my_dict['month'] = int(i[1][3:5])
        my_dict['year'] = int(i[1][-4:])
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


def print_birthdays(current_day, current_month, current_year, user_arr):
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
    for i in range(len(prev_month_data)):
        print('Ранее: nickname: {}, имя: {}, возраст {} '.format(
            prev_month_data[i]['nickname'],
            prev_month_data[i]['name'],
            current_year - prev_month_data[i]['year']
            ))

#
#


if sys.platform[0:6] != 'linux':
    print('This program for Linux only!')
    exit()

if sys.version_info[0] < 3:
    print('This program for Python version >= 3 !')
    exit()

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

nowData = datetime.datetime.now()
nowDateDay, nowDateMonth= nowData.day, nowData.month
nowDateYear = nowData.year

print_birthdays(nowDateDay, nowDateMonth, nowDateYear, userArrDictData)



#print(userArrDictData)
