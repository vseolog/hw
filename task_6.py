import random
# print(random.randint(0,9))
days = ['monday', 'tuesday', 'wednsday', 'thursday', 'friday']
lessons = ['math', 'english', 'physics', 'biology', 'act', 'geography', 'history', 'chemistry', 'russian', 'literatyre']

def get_lesson(lessons):
    return lessons[random.randint(0, (len(lessons)-1))]

# def get_day(days):
#     return days[random.randint(0, (len(days)-1))]

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
        res = self.name + '\n' + self.cab + ' cabinet'
        return res

class Day():
    # date = None #'friday'
    # list = []
    # quantity_of_lessons = len(list)

    def __init__(self, date, list):
        self.date = date
        self.list = list

    def info(self):
        print(self.date + '\n' + str(len(list)) + ' lessons:')
        for i in self.list:
            return i

mn = Lesson()
ts = Lesson()
wen = Lesson()
tr = Lesson()
fr = Lesson()

for i in range(1, (len(days)+1)):
    days[i-1] = a
    a = Day()
    list.append(a)

class Schedule():
    name_of_class = '11C'
    class_type = 'Intramural'
    school = 'School №1594'
    list_of_days = []

    def info(self):
        for i in list_of_days:
            return i


a = Lesson()
print(a.info())
