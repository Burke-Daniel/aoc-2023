def part1(file_name: str):
    with open(file_name, "r") as input:
        total_calibration = 0
        for line in input:
            calibration = "" 
            for char in line:
                if char.isdigit():
                    calibration += char
            if calibration.isdigit():
                total_calibration += int(calibration[0] + calibration[len(calibration) - 1])

        print("total_calibration: {}".format(total_calibration))


def part2(file_name: str):
    digit_strings = [
        "zero", # So that index matches value
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    with open(file_name, "r") as input:
        total_calibration = 0
        for line in input:
            calibration = "" 
            for i in range(len(line)):
                if line[i].isdigit():
                    calibration += line[i]
                else:
                    j = i + 1
                    while j < len(line):
                        substr = line[i:j]
                        if substr in digit_strings:
                            calibration += str(digit_strings.index(substr))
                            break
                        j += 1
            if calibration.isdigit():
                total_calibration += int(calibration[0] + calibration[len(calibration) - 1])

        print("total_calibration: {}".format(total_calibration))


if __name__ == '__main__':
    part1("day1_input.txt")
    part2("day1_input.txt")


