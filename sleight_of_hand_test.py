#ID 85594837
def clever_hands(press, matrix):
    """Функция определения 'ловкости рук'."""
    # Создаём пустой словарь и переменную-счётчик
    incoming_nums = {}
    count = 0
    for i in matrix:
    # Проходим циклом по строке и добавляем в словарь пары:
    # ключ(элемент строки) и значение(сколько раз этот элемент встречается)
        incoming_nums[i] = incoming_nums.setdefault(i, 0) + 1
    for key in incoming_nums.keys():
        # Идём по ключам словаря и проверяем условие: 
        # если значение ключа меньше или равно числу кнопок, 
        # которые, могут нажать ребята -
        # добавляем в переменную-счётчк 1 "балл"
        if incoming_nums[key] <= press:
            count += 1
    return count


if __name__ == '__main__':
    pressing_keys = int(input()) * 2 # Так как ребят двое, сразу умножаем их нажатия на 2
    matrix = str((''.join([input() for _ in range(4)]).replace('.', '')))
    print(clever_hands(pressing_keys, matrix))
