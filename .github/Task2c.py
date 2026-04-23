def increment_all(nums:list[int]) -> list[int]:
    new_list = []
    for value in nums:
        new_list.append(value + 1)     # Record each value of new_list and value at the end of the loop body.
    return new_list                     # 4 is [5], 9 is [5,10], 2 is [5,10,3], 1 is [5,10,3,2]

result = increment_all([4, 9, 2, 1])