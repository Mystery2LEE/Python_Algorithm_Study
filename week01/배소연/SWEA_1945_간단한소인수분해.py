T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    primes = [2, 3, 5, 7, 11]
    counts = [0] * 5

    for i in range(5):
        while N % primes[i] == 0:
            N //= primes[i]
            counts[i] += 1

    print(f'#{tc} ', *counts)