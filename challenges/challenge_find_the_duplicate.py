def find_duplicate(nums: "list[int]"):
    nums.sort()

    number, count = [False, 1]

    for index in range(1, len(nums)):
        cur_number = nums[index]

        if type(cur_number) != int or cur_number < 1:
            return False

        if cur_number == nums[index - 1]:
            number = cur_number
            count += 1

    return number
