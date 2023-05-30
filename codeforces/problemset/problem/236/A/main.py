def main():
    username = input()
    chars = {chr(ord('a') + i): 0 for i in range(26)}
    for i in username:
        chars[i] += 1
    sum = 0
    for i in chars:
        if chars[i] != 0:
            sum += 1
    if sum % 2 == 0:
        print('CHAT WITH HER!')
    else:
        print('IGNORE HIM!')


if __name__ == '__main__':
    main()
