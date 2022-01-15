

from turtle import left
import numpy as np


def binary_search(number=1) -> int:
    """Угадываем число бинарным поиском!
    Args:
        number (int, optional): Загаданное число. Defaults to 1.
    Returns:
        int: Число попыток
    """
    counter = 0
    left = 0 # нижняя граница
    right = 100 # верхняя граница

    while left <= right:
        counter+= 1
        predict_number = (left + right)/2 # поиск среднего значения в промежутке
        
        if number < predict_number:
            right = predict_number - 1 # изменение верхней границы, если число больше загаданного    
        if number > predict_number:
            left= predict_number + 1 # изменение нижней границы, если число меньше загаданного   
        if number == predict_number:
            break  # завершение цикла при условии что числа равны
        
    return counter


def score_game(binary_search) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм
    Args:
        random_predict ([type]): функция угадывания
    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size = (1000))  # загадали список чисел

    for numb in random_array:
        count_ls.append(binary_search(numb))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(binary_search)