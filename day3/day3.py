import pdb
digits = "0123456789"
def part1(file_name: str):
    with open(file_name, "r") as input:
        part_numbers = {}
        lines = []
        for line in input:
            lines.append(line)
        
        for line_num, line in enumerate(lines):
            line = line.rstrip()
            line_length = len(line)
            i = 0
            while i < line_length:
                j = i + 1
                if line[i].isdigit():
                    while j < line_length and line[j] in digits:
                        j += 1
                else:
                    i = j
                    continue
                in_between_vals = [k for k in range(i + 1, j)]
                indices_to_check = {
                    line_num - 1: [i - 1, i, j],
                    line_num: [i - 1, j],
                    line_num + 1: [i - 1, i, j],
                }
                indices_to_check[line_num - 1].extend(in_between_vals)
                indices_to_check[line_num + 1].extend(in_between_vals)

                is_part_number = False
                for ln, indices in indices_to_check.items():
                    for index in indices:
                        if ln in range(0, len(lines)) and index in range(0, line_length):
                            if lines[ln][index] != "." and lines[ln][index] not in digits:
                                is_part_number = True
                                if (ln, index) in part_numbers:
                                    part_numbers[(ln, index)].append(int(line[i:j]))
                                else:
                                    part_numbers[(ln, index)] = [int(line[i:j])]
                                break
                i = j

        total = 0
        for key, val in part_numbers.items():
            for v in val:
                total += v

        print("Answer: {}".format(total))


def part2(file_name: str):
    with open(file_name, "r") as input:
        part_numbers = {}
        lines = []
        for line in input:
            lines.append(line)
        
        for line_num, line in enumerate(lines):
            line = line.rstrip()
            line_length = len(line)
            i = 0
            while i < line_length:
                j = i + 1
                if line[i].isdigit():
                    while j < line_length and line[j] in digits:
                        j += 1
                else:
                    i = j
                    continue
                in_between_vals = [k for k in range(i + 1, j)]
                indices_to_check = {
                    line_num - 1: [i - 1, i, j],
                    line_num: [i - 1, j],
                    line_num + 1: [i - 1, i, j],
                }
                indices_to_check[line_num - 1].extend(in_between_vals)
                indices_to_check[line_num + 1].extend(in_between_vals)

                is_part_number = False
                for ln, indices in indices_to_check.items():
                    for index in indices:
                        if ln in range(0, len(lines)) and index in range(0, line_length):
                            if lines[ln][index] != "." and lines[ln][index] not in digits:
                                is_part_number = True
                                if (ln, index) in part_numbers:
                                    part_numbers[(ln, index)].append(int(line[i:j]))
                                else:
                                    part_numbers[(ln, index)] = [int(line[i:j])]
                                break
                i = j

        total = 0
        for key, val in part_numbers.items():
            if len(val) > 1:
                total += val[0] * val[1]

        print("Answer: {}".format(total))

if __name__ == "__main__":
    part1("day3_input.txt")
    part2("day3_input.txt")
