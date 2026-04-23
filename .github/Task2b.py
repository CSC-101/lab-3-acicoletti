def copy(nums:list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):
        new_list.append(nums[idx])     # Record each value of new_list and idx at the end of the loop body.
    return new_list                    # How does this loop differ from that above?
                                            # idx 0 is [4], idx 1 is [4,9], idx 2 is [4,9,2], idx 3 is [4,9,2,1]
result = copy([4, 9, 2, 1])                 # this loop is adding new values to previous ones