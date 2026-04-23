def tally(nums:list[int]) -> int:
    total = 0
    for num in nums:             # stop on 2 and 3
        total = total + num           # Record each value of total and num at the end of the loop body.
    return total                        # num = 4 is 0, num = 9 is 13, num = 2 is 15, num = 1 is 16

result = tally([4, 9, 2, 1])