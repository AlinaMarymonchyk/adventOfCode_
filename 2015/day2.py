from day1 import read_input


def part_1(input_file: str):
    input = read_input(input_file)
    presents_dimensions = input.split("\n")
    surface = 0
    for present in presents_dimensions:
        l, w, h = present.split("x")
        l, w, h = int(l), int(w), int(h)
        slack = min([l * w, w * h, h * l])
        surface += 2 * l * w + 2 * w * h + 2 * h * l + slack
    print(surface)


def part_2(input_file: str):
    input = read_input(input_file)
    presents_dimensions = input.split("\n")
    ribbon = 0
    for present in presents_dimensions:
        l, w, h = present.split("x")
        l, w, h = int(l), int(w), int(h)
        perimeter = min([2*l+2*h, 2*w+2*h, 2*w+2*l])
        ribbon += perimeter + w*h*l
    print(ribbon)


if __name__ == '__main__':
    part_1("day2.txt")
    part_2("day2.txt")
