def part1(file_name: str):
    red = 0
    green = 1
    blue = 2
    max_possible = [12, 13, 14]
    game_results = [[100, 100, 100]]
    with open(file_name, "r") as input:
        for line in input:
            result = [0, 0, 0]
            for i in range(8, len(line)):
                j = i + 1
                value = 0
                if not line[i:j].isdigit():
                    continue

                while line[i:j].isdigit():
                    value = int(line[i:j])
                    j += 1

                if j < len(line):
                    if line[j] == "r":
                        if value > result[red]:
                            result[red] = value
                    elif line[j] == "g":
                        if value > result[green]:
                            result[green] = value
                    elif line[j] == "b":
                        if value > result[blue]:
                            result[blue] = value
            game_results.append(result)

        answer = 0
        for i in range(len(game_results)):
            if game_results[i][red] <= max_possible[red] and game_results[i][green] <= max_possible[green] and game_results[i][blue] <= max_possible[blue]:
                answer += i

        print("Part 1: {}".format(answer))


def part2(file_name: str):
    red = 0
    green = 1
    blue = 2
    max_possible = [12, 13, 14]
    game_results = [[100, 100, 100]]
    with open(file_name, "r") as input:
        for line in input:
            result = [0, 0, 0]
            for i in range(8, len(line)):
                j = i + 1
                value = 0
                if not line[i:j].isdigit():
                    continue

                while line[i:j].isdigit():
                    value = int(line[i:j])
                    j += 1

                if j < len(line):
                    if line[j] == "r":
                        if value > result[red]:
                            result[red] = value
                    elif line[j] == "g":
                        if value > result[green]:
                            result[green] = value
                    elif line[j] == "b":
                        if value > result[blue]:
                            result[blue] = value
            game_results.append(result)

        answer = 0
        for result in game_results[1:]:
            answer += result[red] * result[green] * result[blue]

        print("Part 2: {}".format(answer))


if __name__ == '__main__':
    part1("day2_input.txt")
    part2("day2_input.txt")
