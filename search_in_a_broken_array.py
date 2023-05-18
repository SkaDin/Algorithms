# ID 87020573
def broken_search(nums: list, target: int) -> int:
    """Функция поиска элменета в сломанном массиве."""
    left_border = 0  # Левая граница массива.
    right_border = len(nums) - 1  # Правая граница массива(по индексу).
    while left_border <= right_border:
        # Высчитываем середину массива
        mid = (left_border + right_border) >> 1
        if nums[mid] == target:
            # Если мы "попали" с первого раза, возвращаем результат.
            return mid
        # Здесь проверяем отношение крайнего левого элемента
        # (и правого) к центральному.
        # И двигаем центр в зависимости от результата сравнений.
        if nums[left_border] <= nums[mid]:
            if nums[left_border] <= target < nums[mid]:
                right_border = mid - 1
            else:
                left_border = mid + 1
        else:
            if nums[mid] < target <= nums[right_border]:
                left_border = mid + 1
            else:
                right_border = mid - 1
    return -1
