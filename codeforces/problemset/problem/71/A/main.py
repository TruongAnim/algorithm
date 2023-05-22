def process(word):
    if len(word)<=10:
        print(word)
    else:
        print(word[0]+str(len(word)-2)+word[-1])


def main():
    # with open('input.txt', 'r') as file:
    #     content = file.read()
    #     lines = content.split('\n')
    #     for i in lines[1:]:
    #         process(i)

    n = int(input())
    for i in range(n):
        process(input())


# Check if this file is being run directly (not imported)
if __name__ == "__main__":
    main()
