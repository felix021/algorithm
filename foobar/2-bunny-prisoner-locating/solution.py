#coding:utf-8
def solution(x, y):
    z = x + y - 1

    # actually it could be simplied to `p = 1 + z * (z - 1) / 2`
    p = 1
    for i in range(2, z + 1):
        p += i - 1

    return str(p + x - 1)

if __name__ == "__main__":
    print solution(3, 2) == "9"
    print solution(5, 10) == "96"