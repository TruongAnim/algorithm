import random
import sys
test = 10

sys.stdout = open('output.txt', 'w')
print(test)
for _ in range(test):
    n = random.randint(1, 10)
    print(n)
    a = [random.randint(0, 10) for i in range(n)]
    for i in range(n):
        print(a[i], end=' ' if i!= n-1 else '\n')
