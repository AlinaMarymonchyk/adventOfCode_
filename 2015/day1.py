import collections


def read_input(file: str):
    with open(file, "r") as f:
        return f.read()


def part_1(input_file: str):
    input = read_input(input_file)
    result = collections.Counter(input)
    floor = result["("] - result[")"]
    print(floor)


def part_2(input_file: str):
    input = read_input(input_file)
    floor = 0
    for i in range(len(input)):
        if input[i] == "(":
            floor += 1
        if input[i] == ")":
            floor -= 1
        if floor == -1:
            print(i+1)
            break


if __name__ == '__main__':
    part_1("day1.txt")
    part_2("day1.txt")

