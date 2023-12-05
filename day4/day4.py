import pdb
def part1(file_name: str):
    with open(file_name, "r") as input:
        points = 0
        for line in input:
            line = line[8:]
            split = line.split("|")
            winning_numbers = split[0].split()
            my_numbers = split[1].split()
            score = 0
            for number in my_numbers:
                if number in winning_numbers:
                    if score == 0:
                        score = 1
                    else:
                        score *= 2
            points += score
        print("Answer: {}".format(points))

            
def part2(file_name: str):
    with open(file_name, "r") as input:
        num_cards = 0
        lines = []
        for line in input:
            lines.append(line)
            num_cards += 1

        multipliers = [1 for i in range(num_cards)]

        # pdb.set_trace()
        for line_num, line in enumerate(lines):
            line = line[8:]
            split = line.split("|")
            winning_numbers = split[0].split()
            my_numbers = split[1].split()
            points = 0
            for number in my_numbers:
                if number in winning_numbers:
                    points += 1

            for i in range(1, points + 1):
                # print(i)
                if line_num + i in range(num_cards + 1):
                    multipliers[line_num + i] += multipliers[line_num]

            # print(multipliers)
        print("Answer: {}".format(sum(multipliers)))



if __name__ == "__main__":
    part1("day4_input.txt")
    part2("day4_input.txt")

