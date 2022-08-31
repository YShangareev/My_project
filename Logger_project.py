import os
import datetime


class Logger:
    time_event = datetime.datetime.now().strftime('%H:%M:%S')
    name = os.path.join('D:\project', 'log_' + datetime.datetime.now().strftime('%d.%m.%Y.'))
    all_logs = os.listdir('D:\project')

    def __init__(self):
        with open(Logger.name, 'w', encoding='utf-8'):
            pass

    @staticmethod
    def write_log():
        event = str(input('Запишите сообщение об ошибке: '))
        with open(Logger.name, 'a', encoding='utf-8') as f:
            f.writelines(f'[{Logger.time_event}] {event}\n')

    @staticmethod
    def data_now():
        return datetime.date.today().strftime('%d.%m.%Y')

    @staticmethod
    def clear_log():
        with open(Logger.name, 'w') as f:
            f.write('')

    @staticmethod
    def get_log():
        with open(Logger.name, 'r', encoding='utf - 8') as f:
            l = f.read().splitlines()
            print(l)

    @staticmethod
    def get_last_event():
        with open(Logger.name, 'r', encoding='utf - 8') as f:
            l = f.read().splitlines()
            print(l[-1])

    @classmethod
    def get_all_logs(cls):
        return Logger.all_logs


l = Logger()

print()
