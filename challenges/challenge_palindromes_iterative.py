def is_palindrome_iterative(word: str):
    word = str(word)
    lenght = len(word)
    if lenght < 1:
        return False

    low_id = 0
    high_id = lenght - 1

    while high_id >= low_id:
        if word[low_id] != word[high_id]:
            return False
        low_id += 1
        high_id -= 1

    return True
