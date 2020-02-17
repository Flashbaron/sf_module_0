import numpy as np
count = 0                            # счетчик попыток
number = np.random.randint(1,100)    # загадали число
print ("Загадано число от 1 до 99")

# for count in range(1,100):         # более компактный вариант счетчика
#     predict = np.random.randint(1,100) # предполагаемое число
#     if number == predict: break    # выход из цикла, если угадали
#     elif number > predict: print (f"Угадываемое число больше {predict} ")
#     elif number < predict: print (f"Угадываемое число меньше {predict} ")
#
# print (f"Вы угадали число {number} за {count} попыток.")

def game_core_v3(number, random_num_min, random_num_max):
    """
    Использование метода половинного деления для максимально
    быстрого автоматизированного решения задачи.
    В результате алгоритм в среднем решается за 5 попыток.
    https://ru.wikipedia.org/wiki/%D0%9C%D0%B5%D1%82%D0%BE%D0%B4_%D0%B1%D0%B8%D1%81%D0%B5%D0%BA%D1%86%D0%B8%D0%B8
    """

    count = 1 # Всегда есть минимум одна попытка
    predict = random_num_max // 2 # Среднее между минимальным и максимальным
    while number != predict:
        count += 1
        if predict > number:
            # random_num_max берётся из среднего, а predict - снова среднее между минимальным и новым максимальным
            random_num_max = predict
            predict = random_num_min + ((random_num_max - random_num_min) // 2)
        else:
            # то же самое, но наоборот
            random_num_min = predict
            predict = random_num_min + ((random_num_max - random_num_min) // 2)+1

            """Если не прибавлять единицу, программа попадает в бесконечный
            цикл, т.к. // всегда будет округлять число в меньшую сторону, что
            в итоге приведёт к суммированию нуля"""
    return count


def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его
       в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0 # Должно быть 1 !!
    predict = np.random.randint(1,100)
    while number != predict:
        count+=1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return(count) # выход из цикла, если угадали




def score_game(game_core):
    '''Запускаем игру 1000 раз, чтоб узнать как быстро игра угадывает число'''
    """Печатает и возвращает ср.знач, за которое угадывается число"""
    count_ls = [] # Счётчик количества отгадываний
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_num_min = 1
    random_num_max = 99 # максимальное случайное число
    random_array = np.random.randint(random_num_min, random_num_max+1, size=(1000)) # создаёт 1000 случайных чисел от 1 до 100
    for number in random_array:
        count_ls.append(game_core(number, random_num_min, random_num_max))
    score = int(np.mean(count_ls)) # среднее число
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

# запускаем
score_game(game_core_v3)
