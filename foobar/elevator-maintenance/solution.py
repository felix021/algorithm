def solution(l):
    def cmpVersion(x, y):
        xvalues = map(int, x.split("."))
        yvalues = map(int, y.split("."))
        while len(xvalues) < len(yvalues):
            xvalues.append(-1)
        while len(xvalues) > len(yvalues):
            yvalues.append(-1)
        for xi, yi in zip(xvalues, yvalues):
            if xi < yi:
                return -1
            elif xi > yi:
                return 1
        return 0

    return list(sorted(l, cmp=cmpVersion))


def cmplists(a, b):
    if len(a) != len(b):
        return False
    for x, y in zip(a, b):
        if x != y:
            return False
    return True

if __name__ == "__main__":
    print(cmplists(
        solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]),
        ["0.1", "1.1.1", "1.2", "1.2.1", "1.11", "2", "2.0", "2.0.0"]
    ))
    print(cmplists(
        solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]),
        ["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"]
    ))