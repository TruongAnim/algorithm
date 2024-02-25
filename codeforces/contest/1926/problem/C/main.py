# https://codeforces.com/contest/1926/problem/C

def sum_of_digits(number):
    # Convert the number to a string to iterate through its digits
    num_str = str(number)

    # Initialize a variable to store the sum
    digit_sum = 0

    # Iterate through each digit in the string and add it to the sum
    for digit in num_str:
        digit_sum += int(digit)

    return digit_sum


def main():
    test = int(input())
    A = [0 for i in range(200001)]
    pre = 0
    s = 0
    for i in range(0, 200001):
        if i % 10 == 0:
            pre = sum_of_digits(i)
            s += pre
        else:
            pre = pre + 1
            s += pre
        A[i] = s
    for t in range(test):
        n = int(input())
        print(A[n])


if __name__ == '__main__':
    main()
