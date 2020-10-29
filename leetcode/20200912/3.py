# source: https://leetcode-cn.com/contest/season/2020-fall/problems/UlBDOe/

class Solution(object):
    def minimumOperations(self, leaves):
        """
        :type leaves: str
        :rtype: int
        """
        n = len(leaves)
        head_r = [0] * n
        head_ry = [n] * n
        left_reds = 0
        for i in range(n):
            if leaves[i] == 'r':
                left_reds += 1
            head_r[i] = i + 1 - left_reds
            if i > 0:
                head_ry[i] = min(
                    head_r[i-1]  + (1 if leaves[i] == 'r' else 0),
                    head_ry[i-1] + (1 if leaves[i] == 'r' else 0),
                )

        tail_r = [0] * n
        tail_yr = [n] * n
        right_reds = 0
        for j in range(n - 1, -1, -1):
            if leaves[j] == 'r':
                right_reds += 1
            tail_r[j] = n - j - right_reds
            if j < n - 1:
                tail_yr[j] = min(
                    tail_r[j+1]  + (1 if leaves[j] == 'r' else 0),
                    tail_yr[j+1] + (1 if leaves[j] == 'r' else 0),
                )
        
        result = n
        for i in range(1, n - 1):
            result = min(
                result,
                head_r[i] + tail_yr[i + 1],
                head_ry[i] + tail_r[i + 1],
                head_ry[i] + tail_yr[i + 1]
            )

        return result

    def minimumOperationsSlow(self, leaves):
        """
        :type leaves: str
        :rtype: int
        """
        right_yellow = [0] * len(leaves)
        n = 0
        for i in range(len(leaves) - 1, -1, -1):
            if leaves[i] == 'y':
                n += 1
            right_yellow[i] = n
        
        left_red = [0] * len(leaves)
        n = 0
        for i in range(0, len(leaves)):
            if leaves[i] == 'r':
                n += 1
            left_red[i] = n

        yellow_red = [0] * len(leaves)
        for i in range(len(leaves) - 1):
            yellow_red = left_red[i] + right_yellow[i]

        result = None
        left_yellow = 0
        for i in range(0, len(leaves) - 2):
            if leaves[i] == 'y':
                left_yellow += 1
            yr = None
            for j in range(i + 1, len(leaves) - 1):
                x = left_red[j] - left_red[i] + right_yellow[j+1]
                yr = min(yr, x) if yr is not None else x
            x = left_yellow + yr
            result = min(result, x) if result is not None else x
        return result


if __name__ == "__main__":
    import sys
    s = Solution()
    print s.minimumOperations("ryr") == 0
    print s.minimumOperations("rrr") == 1
    print s.minimumOperations("yry") == 3
    print s.minimumOperations("yrry") == 3
    print s.minimumOperations("yryry") == 2
    print s.minimumOperations("rrryyyryyyrr") == 1
    print s.minimumOperations("rrryyyrryyyrr") == 2
    print s.minimumOperations("ryrrrrrrrrryr") == 1