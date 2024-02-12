# ТЗ:
# Создать 3 класса, описывающие школьное расписание на неделю 
# (Расписание, День, Занятие). заполнить данными и реализовать
# классы расписание и День недель как итерируемые объекты 


import random
# print(random.randint(0,9))
days = ['monday', 'tuesday', 'wednsday', 'thursday', 'friday']
lessons = ['math', 'english', 'physics', 'biology', 'act', 'geography', 'history', 'chemistry', 'russian', 'literatyre', 'geometry']

def get_lesson(lessons):
    return lessons[random.randint(0, (len(lessons)-1))]

def get_day(days):
    return days[random.randint(0, (len(days)-1))]

def get_cab():
    a = random.randint(1, 5)
    b = random.randint(1, 30)
    if b < 10:
        b = '0' + str(b)
    res = str(a) + str(b)
    return res


class Lesson():
    # name = get_lesson(lessons)
    # # time = None #'12:00-12:45'
    # cab = get_cab()
    def __init__(self):
        self.name = get_lesson(lessons)
        self.cab = get_cab()

    def info(self):
        res = self.name + '; ' + self.cab + ' cabinet'
        return res

class Day():
    # date = None #'friday'
    # list = []
    # quantity_of_lessons = len(list)

    def __init__(self, date, start, quantity_of_lessons):
        self.date = days[(date % 5) - 1]
        self.start = start
        self.quantity_of_lessons = quantity_of_lessons
        self.list = []
        k = 0
        while k < self.quantity_of_lessons:
            self.list.append(Lesson())
            k += 1

    def info(self):
        print(self.date.capitalize() + ':')
        for i in self.list:
            n = self.list.index(i) + 1
            m = str(self.start + n - 1)
            res = str(n)+ '. ' + m + ':00-' + m + ':45 ' + i.info()
            print(res)
        return '-' * len(res)


# a = Day(8, 8)
# print(a.info())

class Schedule():
    # name_of_class = '11C'
    # class_type = 'Intramural'
    # school = 'School №1594'
    # list_of_days = []

    def __init__(self, quantity_of_days):
        self.number_of_week = random.randint(1, 20)
        self.quantity_of_days = quantity_of_days
        self.list = []
        k = 0
        while k < quantity_of_days:
            self.list.append(Day((k + 1), 8, 8))
            k += 1
    
    def info(self):
        print('Week ' + str(self.number_of_week) + ' :' + '\n')
        for i in self.list:
            print(i.info() + '\n')
        return '#' * 38

a = Schedule(5)
print(a.info())

# -------------------------------------------------------------------------
# -------------------------------------------------------------------------

# b=[]
# k=0
# quantity_of_lessons = 7
# while k < quantity_of_lessons:
#     b.append(Lesson())
#     k +=1

# for i in b:
#     start = 8
#     n = b.index(i)+1
#     m = str(start+n-1)
#     print(str(n)+ '. ' + m + ':00-' + m + ':45 ' + i.info())



# mn = Lesson()
# ts = Lesson()
# wen = Lesson()
# tr = Lesson()
# fr = Lesson()

# for i in range(1, (len(days)+1)):
#     days[i-1] = a
#     a = Day()
#     list.append(a)
