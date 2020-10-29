# source: https://leetcode-cn.com/contest/season/2020-fall/problems/2vYnGI/

class Solution(object):
    def breakfastNumber(self, staple, drinks, x):
        """
        :type staple: List[int]
        :type drinks: List[int]
        :type x: int
        :rtype: int
        """
        staple.sort()
        drinks.sort()

        result = 0
        for s in staple:
            d = self.upper_bound(drinks, x - s)
            result = (result + d) % 1000000007
        
        return result

    @staticmethod
    def upper_bound(s, x):
        left, right = 0, len(s)
        while left < right:
            mid = (left + right) / 2
            if s[mid] <= x:
                left = mid + 1
            else: # s[mid] > x
                right = mid
        return right


if __name__ == "__main__":
    s = Solution()
    print s.breakfastNumber([10, 20, 5], [5, 5, 2], 15) == 6
    print s.breakfastNumber([2, 1, 1], [8, 9, 5, 1], 9) == 8