def is_anagram(first_string: str, second_string: str):
    if first_string == '' and second_string == '':
        return (first_string, second_string, False)

    first_lower = list(first_string.lower())
    second_lower = list(second_string.lower())
    merge_sort(first_lower)
    merge_sort(second_lower)

    first_lower = "".join(first_lower)
    second_lower = "".join(second_lower)

    result = first_lower == second_lower

    return (first_lower, second_lower, result)


# Merge Sort auxiliar
# Referência: https://www.youtube.com/watch?v=5prE6Mz8Vh0&ab_channel=Programa%C3%A7%C3%A3oDin%C3%A2mica
def merge_sort(word, start=0, end=None):
    if end is None:
        end = len(word)
    if (end - start) > 1:
        mid = (end + start) // 2
        merge_sort(word, start, mid)
        merge_sort(word, mid, end)
        merge(word, start, mid, end)


def merge(word, start, mid, end):
    left = word[start:mid]
    right = word[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            word[general_index] = right[right_index]
            right_index += 1
        elif right_index >= len(right):
            word[general_index] = left[left_index]
            left_index += 1
        elif left[left_index] < right[right_index]:
            word[general_index] = left[left_index]
            left_index += 1
        else:
            word[general_index] = right[right_index]
            right_index += 1
