# source: https://leetcode-cn.com/contest/season/2020-fall/problems/nGK0Fy/

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        x, y = 1, 0
        for c in s:
            if c == 'A':
                x = 2 * x + y
            elif c == 'B':
                y = 2 * y + x
            else:
                raise Exception("XXX")
        return x + y


if __name__ == "__main__":
    s = Solution()
    print s.calculate('AB') == 4