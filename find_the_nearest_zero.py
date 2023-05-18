#ID 85591591
from typing import List
def nearest_zero(lenght: int, numbers: List) -> List: 
    """Функция нахождения 'ближайшего нуля'."""
    # в переменной-счётчике сразу предусматриваем случай,
    # когда последовательность начинается не с нуля
    count = lenght if numbers[0] != 0 else 0
    for i in range(lenght):
        # Проходим циклом по диапазону длинны массива проверяя,
        # равен ли очередной элемент нулю и если да - записываем ноль
        # и сбрасываем переменную-счётчик
        if numbers[i] == 0:
            count = 0
        else:
            count += 1
            numbers[i] = count 
            # если число отлично от нуля увеличиваем переменную-счётчик на 1
            # и указываем что элемент массива теперь "равен" переменной-счётчику
    for j in range(lenght - 1, -1, -1):
        # здесь мы идёт по массиву в обратном направлении
        # аналогично проверяя условие как и в первом цикле
        if numbers[j] == 0:
            count = 0
        else:
            count += 1
            # отличие от первого цикла, мы выбираем нименьшее значение между:
            # переменной-счётчиком и элементом(индексом массива)
            numbers[j] = min(count, numbers[j])
    return numbers


if __name__ == '__main__':
    lenght = int(input())
    number_house = [int(n) for n in input().split()]
    print(*nearest_zero(lenght, number_house))
