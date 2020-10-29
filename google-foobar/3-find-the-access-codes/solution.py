def solution(l):
    div = {}
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[j] % l[i] == 0:
                if i in div:
                    div[i].append(j)
                else:
                    div[i] = [j]

    cnt = 0
    for i, idiv in sorted(div.items()):
        for j in idiv:
            jdiv = div.get(j, [])
            cnt += len(jdiv)

    return cnt

if __name__ == "__main__":
    print(solution([1,2,3,4,5,6]) == 3)
    print(solution([1,1,1]) == 1)
    print(solution([1,1,1,1]) == 4)
     