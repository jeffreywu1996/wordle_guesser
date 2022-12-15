

def can_sum(sum: int, arr: [int]) -> bool:
    if len(arr) == 0:
        return False

    if sum in arr:
        return True

    if sum < 0:  # dont support negative sums
        return False

    success = False
    for val in arr:
        if sum - val < 0:
            continue

        suc = can_sum(sum - val, arr.remove(val))
        if suc:
            success = suc


    return True
