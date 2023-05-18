# ID 87075838
# Это  изменённая работа с учётом  замечаний "Можно лучше".
import random


def partition(arr: list, left: int, right: int) -> int:
    """Функция разделения списка."""
    # Случайно выбираем случайный индекс элемента(он же будет опорным),
    # затем меняем местами элемент array[left] с
    # элементом array[random_index].
    # Это нужно для того, чтобы текущий опорный элемент
    # оказался в начале списка (по индексу left).
    random_index = random.randint(left, right - 1)
    arr[left], arr[random_index] = arr[random_index], arr[left]
    pivot = arr[left]  # Опорный элемент.
    lf_border = left + 1  # Левая граница.
    rg_border = right - 1  # Правая граница.
    # Далее основной цикл который продолжается пока левая граница
    # не пересечётся с правой.
    # Внутри цикла двигаем границы left_border и right_border
    # к центру списка, пока не найдутся элементы,
    # которые нужно поменять местами.
    while True:
        while lf_border <= rg_border and arr[rg_border] > pivot:
            rg_border -= 1
        while lf_border <= rg_border and arr[lf_border] < pivot:
            lf_border += 1
        # Если левая граница не больше правой границы,
        # то найденные элементы меняются местами.
        if lf_border <= rg_border:
            arr[lf_border], arr[rg_border] = arr[rg_border], arr[lf_border]
        # Если же границы пересеклись, то опорный элемент
        # меняется местами с элементом,
        # находящимся первым справа от границы.
        else:
            arr[left], arr[rg_border] = arr[rg_border], arr[left]
        # Возвращаем индекс right_border, который показывает,
        # где закончилась левая часть списка,
        # и начинается правая(все элементы, больше опорного).
            return rg_border


def quick_sort(array: list, left: int, right: int) -> None:
    """Функция сортировки списка."""
    # Рекурсивно вызываем массив пока подсписки не будут упорядочены.
    if right - left > 1:
        pivot_index = partition(array, left, right)
        quick_sort(array, left, pivot_index)
        quick_sort(array, pivot_index + 1, right)


class Participant(object):
    """Класс участника."""

    __slots__ = ['username', 'points', 'penalty']

    def __init__(self, username: str, points: int, penalty: int):
        self.username = username
        self.points = points
        self.penalty = penalty

    def __str__(self) -> str:
        """Возврат имени участника."""
        return f'{self.username}'

    def __lt__(self, other) -> bool:
        """Перегрузка метода сравнения(<)."""
        # Метод возвращает True если:
        # если количество набранных очков у первого участника больше,
        # чем у второго участника,
        # иначе сравнивает количество штрафных очков.
        # Если количество очков у двух участников равно
        # и количество штрафных очков у первого участника меньше,
        # чем у второго, или снова равно,
        # но имя первого участника лексикографически меньше,
        # чем имя второго.
        return (self.points > other.points) or \
            (self.points == other.points and
             (self.penalty < other.penalty or
              (self.penalty == other.penalty and self.username < other.username)))


if __name__ == '__main__':
    number_participants = int(input())
    participants = []
    for _ in range(number_participants):
        name, points, penalty = input().split()
        participant = Participant(name, int(points), int(penalty))
        participants.append(participant)
    quick_sort(participants, 0, len(participants))
    names = [str(participant) for participant in participants]
    print(*names, sep='\n')
