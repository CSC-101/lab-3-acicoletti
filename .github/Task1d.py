def inc(m:int) -> int:
    return m + 1                             # Record, in order of the calls, each value of m and
                                             # the corresponding return value. 3 is 4, 4 is 5


def check(n:int) -> bool:
    return n > 2                             # Record, in order of the calls, each value of n and
                                             # the corresponding return value. 0 is False, 1 is False, 2 is False, 3 is True


answer = [inc(x) for x in range(5) if check(x)]   # What is the value of answer? [4,5]
print()