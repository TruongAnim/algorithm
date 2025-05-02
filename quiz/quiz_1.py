# Đề bài: Từ ba chữ số tạo thành 6 số có ba chữ số khác nhau.
# Tổng của 6 số này là 2886.
# Hỏi trong 6 số có ba chữ số khác nhau này, số nhỏ nhất là bao nhiêu?


def get_list_6_number(number):
    a,b,c = [i for i in str(number)]
    temp = sorted(map(int, [a+b+c, a+c+b, b+c+a, b+a+c, c+a+b, c+b+a]))
    if len(temp) == len(set(temp)):
        return temp
    return None


def main():
    for i in range(100, 1000):
        list_number = get_list_6_number(i)
        if list_number is not None:
            s = sum(list_number)
            print(s)
            if s == 2886:
                print(list_number)


if __name__ == '__main__':
    main()