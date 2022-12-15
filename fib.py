import sys
sys.setrecursionlimit(5000)

import time


class Solution:
    def climbStairs(self, n: int) -> int:
        # mapping = dict()
        # return self.helper_climbStairs(n, mapping)
        return self.old_climbStairs(n)
        # return self.bottom_up_climbStairs(n)



    def bottom_up_climbStairs(self, n: int) -> int:
        mapping = dict()

        mapping[1] = 1
        mapping[2] = 2
        for i in range(3, n):
            mapping[i] = mapping[i-1] + mapping[i-2]

        return mapping[n-1] + mapping[n-2]

    def helper_climbStairs(self, n: int, mapping: dict) -> int:
        if n in mapping:
            return mapping[n]

        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2

        save = self.helper_climbStairs(n-1, mapping) + self.helper_climbStairs(n-2, mapping)
        mapping[n] = save
        return save

    def old_climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2

        return self.old_climbStairs(n-1) + self.old_climbStairs(n-2)


s = Solution()
start = time.time()
result = s.climbStairs(30)
end = time.time()
print(result)
print(f"Took {(end - start) *1000} seconds")
