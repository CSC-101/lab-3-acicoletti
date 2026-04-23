def check(n:int) -> bool:
    return n > 2                             # Record, in order of the calls, each value of n and
                                             # the corresponding return value. 0 -> False 1-> False 2-> False 3-> True 4-> True


answer = [x for x in range(5) if check(x)]   # What is the value of answer? answer = [3,4]