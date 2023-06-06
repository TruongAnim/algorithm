def main():
    number1 = input()
    number2 = input()
    for i,j in zip(number1, number2):
        if i!=j:
            print(1, end='')
        else:
            print(0, end='')


if __name__=='__main__':
    main()