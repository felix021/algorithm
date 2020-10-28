#!/usr/bin/python

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n == 3:
            return sum(nums)

        nums.sort()
        ans = sum(nums[0:3])

        for i in range(n - 2):
            j, k = i + 1, n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if abs(target - s) < abs(target - ans):
                    ans = s
                if s == target:
                    return target
                elif s > target:
                    k -= 1
                else:
                    j += 1
        return ans


    def threeSumClosestBinarySearch(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n == 3:
            return sum(nums)

        min_diff = 99999999
        ans = 0

        nums.sort()
        for i in range(n):
            for j in range(i + 1, n):
                p = self.lowerBound(nums, target - nums[i] - nums[j])

                # smaller one
                k = p
                while k >= 0:
                    if k == n or k == i or k == j:
                        k -= 1
                        continue
                    s = nums[i] + nums[j] + nums[k]
                    cdiff = abs(target - s)
                    if cdiff < min_diff:
                        min_diff = cdiff
                        ans = s
                    break
                
                # larger one
                k = p
                while k < n:
                    if k == i or k == j:
                        k += 1
                        continue
                    s = nums[i] + nums[j] + nums[k]
                    cdiff = abs(target - s)
                    if cdiff < min_diff:
                        min_diff = cdiff
                        ans = s
                    break

        return ans

    def lowerBound(self, nums, x):
        l, r = 0, len(nums)
        while l < r:
            m = (l + r) / 2
            if nums[m] < x:
                l = m + 1
            else:
                r = m
        return l


if __name__ == "__main__":
    s = Solution()
    print s.threeSumClosest([-1,2,1,-4], 1)