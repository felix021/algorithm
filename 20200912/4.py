# source: https://leetcode-cn.com/contest/season/2020-fall/problems/meChtZ/
# (not solved)

"""

f(x) = min(
    f(x - 1) + inc,
    f(x + 1) + dec,
    [f(x / jump[i]) + cost[i] for i in range(m)]
)

f(target)

"""

class Solution(object):
    def busRapidTransit(self, target, inc, dec, jump, cost):
        """
        :type target: int
        :type inc: int
        :type dec: int
        :type jump: List[int]
        :type cost: List[int]
        :rtype: int
        """
        cache = {0: 0}
        def f(x):
            if x not in cache:
                ans = f(x + 1) + dec
                if x > 0:
                    ans = min(ans, f(x - 1) + inc)
                for j, c in zip(jump, cost):
                    if x % j == 0:
                        ans = min(ans, f(x / j) + c)
                cache[x] = ans
            return cache[x]
        return f(target)

s = Solution()
print s.busRapidTransit(31, 5, 3, [6], [10])