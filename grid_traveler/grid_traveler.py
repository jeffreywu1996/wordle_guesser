
def grid_traveler(m, n):
    # return _recursion_gt(m, n)
    return _top_down_gt(m, n)


def _recursion_gt(m, n):
    if m == 0 or n == 0:
        return 0
    if m == 1 and m == n:
        return 1

    return grid_traveler(m - 1, n) + grid_traveler(m, n - 1)


def _top_down_gt(m, n):
    mem = dict()
    return __top_down_gt_helper(m, n, mem)

def __top_down_gt_helper(m, n, mem):
    if m == 0 or n == 0:
        return 0
    if m == 1 and m == n:
        return 1

    key = f"{m}, {n}"
    if key in mem:
        return mem[key]

    mem[key] = __top_down_gt_helper(m - 1, n, mem) + __top_down_gt_helper(m, n - 1, mem)

    return mem[key]
