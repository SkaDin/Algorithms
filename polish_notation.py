#ID 86123555
import operator

class Stack:
    """Реализация постфиксной нотации при помощи стека(на основе массива)."""

    def __init__(self) -> None:
        self.__items: list = []

    def is_empty(self) -> bool:
        """Метод проверки пустоты стека."""
        return self.__items == []

    def push(self, item: int) -> None:
        """Метод добавления элемента на вершину стека."""
        self.__items.append(item)

    def pop(self) -> int:
        """Метод удаления элемента c вершины стека."""
        elem = self.__items.pop()
        return elem

operator_and_action = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv
}

def chek_type(n):
    if isinstance(n, int):
        return int(n)
    elif isinstance(n, float):
        return float(n)
    elif type(n) == complex:
        return complex(n)
    else:
        return str(n)

def postfix_notation(seq: list) -> int:
    """Функция подсчёта постфиксной последовательности."""
    # Cоздаём словарь, ключами которого будут строки с математическими
    # символами, а значениями методы модуля operator.
    #operator_and_action = {
    #    '+': operator.add,
    #    '-': operator.sub,
    #    '*': operator.mul,
    #    '/': operator.floordiv
    #}
    for _ in seq:
        # Если элемент не ключ словаря(не оператор),
        # добавляем элемент в стек.
        if _ not in operator_and_action.keys():
            stack.push(chek_type(_))
        else:
            # Извлекаем верхний элемент -
            # следующй, проводим арифметические действия
            # и возвращаем на верхушку стека.
            top_elem = stack.pop()
            next_elem = stack.pop()
            result = operator_and_action[_](next_elem, top_elem)
            stack.push(result)
    return stack.pop()


if __name__ == '__main__':
    stack = Stack()
    sequence = []
    for elem in input().split():
        if elem not in operator_and_action.keys():
            sequence.append(int(elem))
            if isinstance(elem, float):
                sequence.append(float(elem))
        else:
            sequence.append(str(elem))
    #sequence = [_ for _ in input().split()]
    print(postfix_notation(sequence))
