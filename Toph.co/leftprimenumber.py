class Solution:
    def find_prime(n: int):
        A = [True] * (n + 1)
        A[0] = A[1] = False
        for i in range(2, int(n**0.5) + 1):
            if A[i]:
                j = i * i
                while j <= n:
                    A[j] = False
                    j += i
        primes = [i for i in range(2, n + 1) if A[i]]
        number=len(primes)
        return number


x=int(input())
list_of_number=[int(input()) for v in range(x)]
for i in list_of_number:
    x=Solution.find_prime(i)
    print(x)


# Without Class 


def find_prime(n: int):
        if n <= 1:
             return 0
        A = [True] * (n + 1)
        A[0] = A[1] = False
        for i in range(2, int(n**0.5) + 1):
            if A[i]:
                j = i * i
                while j <= n:
                    A[j] = False
                    j += i
        primes = [i for i in range(2, n + 1) if A[i]]
        number=len(primes)
        return number

x=int(input())
list_of_number=[int(input()) for v in range(x)]
for i in list_of_number:
    x=find_prime(i)
    print(x)