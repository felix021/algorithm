def solution(n):
    n = int(n)
    digits = []
    while n > 0:
        digits.append(int(n % 2))
        n /= 2
    
    ans = 0
    while digits != [1]:
        # even
        next_zeros = 0
        for i in range(0, len(digits)):
            if digits[i] == 1:
                break
            next_zeros += 1
        if next_zeros > 0:
            digits = digits[next_zeros:]
            ans += next_zeros
            continue

        # odd

        next_ones = 0
        for i in range(len(digits)):
            if digits[i] == 0:
                break
            next_ones += 1

        if next_ones >= 2:
            if len(digits) == 2:
                return ans + 2

            digits = digits[next_ones:]
            ans += next_ones + 1
            if len(digits) == 0:
                return ans
            digits[0] = 1
        else:
            digits[0] = 0
            ans += 1

    return ans


if __name__ == "__main__":
    import sys
    print(solution("1") == 0)
    print(solution("2") == 1)
    print(solution("3") == 2)
    print(solution("4") == 2)
    print(solution("5") == 3)
    print(solution("6") == 3)
    print(solution("7") == 4)
    print(solution("8") == 3)
    print(solution("15") == 5)
    print(solution("59") == 8)
    print(solution("119") == 9)
    print(solution("309") == 12)
    print(solution("495") == 11)
    print(solution("509") == 11)
    print(solution('999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999') == 1278)
    sys.exit(0)