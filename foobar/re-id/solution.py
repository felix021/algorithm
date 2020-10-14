def solution(i):
    nPrime = i + 5
    maxNumber = nPrime * 12  # prime[10000] = 103079
    primes = []
    isPrime = [True] * maxNumber

    for p in range(2, maxNumber):
        if isPrime[p]:
            primes.append(str(p))
            if len(primes) == nPrime:
                break
            for q in range(p + p, maxNumber, p):
                isPrime[q] = False
        
    longString = ''.join(primes)
    return longString[i:i+5]

if __name__ == "__main__":
    print(solution(0))
    print(solution(3))
    print(solution(5))
    print(solution(100))
    print(solution(10000))