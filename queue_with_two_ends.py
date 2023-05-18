#ID 86124177
class Deque:
    """
    Реализация очереди c двумя концами(Дек).
    Ha кольцевом буфере.
    """

    def __init__(self, max_lenght: int) -> None:
        self.__deque: list = [None] * max_lenght
        self.__max_size: int = max_lenght
        self.__right: int = 0
        self.__left: int = 0
        self.__size: int = 0

    def is_empty(self) -> bool:
        """Метод определения пустоты дека."""
        return self.__size == 0

    def push_front(self, item: int) -> None:
        """Метод вставки элемента в конец дека."""
        # Заполненность дека не должна быть равна его длинне(размеру).
        # Иначе поднимаем исключение о том что дек заполнен.
        if self.__size == self.__max_size:
            raise OverflowError
        self.__deque[self.__left] = item
        # После добавления элемента, увеличиваем значение left,
        # как бы передвигая навстречу к right.
        self.__left = (self.__left + 1) % self.__max_size
        self.__size += 1

    def push_back(self, item: int) -> None:
        """Метод вставки элемента в начало дека."""
        if self.__size == self.__max_size:
            raise OverflowError
        # Т.к добавление идёт с конца дека, значение 
        # right изначально указывает на конец дека,
        # и каждый добавленный элемент в конец дека
        # добавляется на последнюю позицию(-1).
        self.__deque[self.__right - 1] = item
        self.__right = (self.__right - 1) % self.__max_size
        self.__size += 1

    def pop_front(self) -> int:
        """
        Метод удаления c начала дека ближайшего к right
        элемента.
        """
        if self.is_empty():
        # Если дек пуст, поднимаем исключение,
        # что в деке нет элементов.
            raise IndexError
        # Записываем в переменную значение left,
        # ближайшего к right элемента.
        value = self.__deque[self.__left - 1]
        # Cтавим на место значения - None.
        self.__deque[self.__left - 1] = None
        # "Передвигаем значение на еденицу влево".
        self.__left = (self.__left - 1) % self.__max_size
        self.__size -= 1 
        return value

    def pop_back(self) -> int:
        """
        Метод удаления c конца дека ближайшего к left
        элемента.
        """
        if self.is_empty():
            raise IndexError
        # Записываем в переменную значение right
        # ближайшего к left элемента.
        value = self.__deque[self.__right]
        # Cтавим на место значения - None.
        self.__deque[self.__right] = None
        # "Передвигаем значение на еденицу вправо".
        self.__right = (self.__right + 1) % self.__max_size
        self.__size -= 1
        return value


def main():
    # Заводим словарь ключами которого будут принимаемые команды,
    # а значениями - вызываемые методы класса.
    commands_check = {
        'push_front': deque.push_front,
        'push_back': deque.push_back,   
        'pop_front': deque.pop_front,
        'pop_back': deque.pop_back,
    }
    for _ in range(commands):
        command = input()
        # Разбиваем строку на 2 части:
        # action(команда) и value (значение(если есть)).
        action, *value = command.split()
        # Если значение есть,
        # вызываем функцию из словаря commands_check
        # и подставляем значение(преобразованное в чилсло).
        # Пример: deque.push_front(861).
        if value:
            try:
                result = commands_check[action](int(*value))
                if result is not None:
                    print(result)
            except OverflowError:
                print('error') 
        else:
            try:
                # Cлучай, когда значения нет.
                result = commands_check[action]()
                print(result)
            except IndexError:
                print('error')


if __name__ == '__main__':
    commands = int(input())
    deque_size = int(input())
    deque = Deque(deque_size)
    main()
