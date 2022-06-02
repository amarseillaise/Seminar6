#  1. Напишите программу, удаляющую из текста все слова, содержащие "абв".

def task1():
    result = ''
    sourceString = 'Напишите програбвамму, удаляющую из текабвста все слова, содержащие "абв".'.split(' ')
    filterResult = list(filter(lambda x: 'абв' not in x, sourceString))
    for h in filterResult:  # Вот не нравится мне этот цикл. Можно ли вместо него использовать что-то "питоновское"?
        result += h + ' '
    return result[:-1]


# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def task2():
    def check(checkingList):
        result = 1
        for i in checkingList:
            result *= i
        return result

    def searchDigit(j, t):
        if j == 1:
            j = t
        if (2 ** j) % j == 2 % j and t % j == 0:  # проверка числа на простоту Малой теоремой Ферма
            myList.append(j)
            t //= j
            j = t
        if check(myList) == n:
            return myList
        else:
            searchDigit(j - 1, t)
            return myList

    n = int(input('Задайте число от 1 до 1000: '))
    myList = []
    if (2 ** n) % n == 2 % n:
        myList.append(n)
        return myList
    else:
        return searchDigit(n, n)

#  3. Реализовать программу, получающую на вход строку, состоящую из слов, разделенных пробелами
#  и возвращающую длину каждого слова.
#  Пример: "Солнце небо воздух земля" --> 6 4 6 5

def task3():
    myString = 'В победе бессмертных идей коммунизма мы видим грядущее нашей страны'.split(' ')
    lenMyString = list(map(lambda x: len(x), myString))
    return lenMyString


# print(task1())
# print(task2())
# print(task3())
