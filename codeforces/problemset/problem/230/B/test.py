# https://codeforces.com/problemset/problem/230/B
import math

import random
import time


def generate_random_numbers(count, start, end):
    random_numbers = []
    for _ in range(count):
        random_number = random.randint(start, end)
        random_numbers.append(random_number)
    return random_numbers


count = 100000
start = 10 ** 11
end = 10 ** 12

random_numbers = generate_random_numbers(count, start, end)


def main():
    count = 0
    primes = prime_filter()
    print(len(primes))
    for i in [350337323449 for _ in range(10 ** 5)]:
        s = int(math.sqrt(i))
        if s in primes and s ** 2 == i:
            count += 1
    print(count)


def check_prime(n):
    if n % 2 == 0:
        return False
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False
    return True


def prime_filter():
    a = [i for i in range(10 ** 6)]
    result = set()
    for i in range(2, len(a)):
        if a[i] != 0:
            result.add(a[i])
            for j in range(a[i], 10 ** 6, a[i]):
                a[j] = 0

    return result


if __name__ == '__main__':
    start_time = time.time()
    main()
    # prime_filter()

    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Elapsed time:", elapsed_time, "seconds")
