import java.io.*;

public class Solution{
    public static String solution(int i) {
        int nPrime = i + 5;
        int maxNumber = nPrime * 12; // prime[10000] = 103079
        int n = 0;
        String[] primes = new String[maxNumber];
        boolean[] isNotPrime = new boolean[maxNumber];

        for (int p = 2; p < maxNumber; p++) {
            if (isNotPrime[p])
                continue;
            
            primes[n] = "" + p;
            n += 1;
            if (n >= nPrime) {
                break;
            }
            for (int q = p + p; q < maxNumber; q += p) {
                isNotPrime[q] = true;
            }
        }

        String longString = String.join("", primes);
        return longString.substring(i, i + 5);
    }

    public static void main(String[] args) {
        System.out.println(solution(0));
        System.out.println(solution(3));
        System.out.println(solution(5));
        System.out.println(solution(10000));
    }
}