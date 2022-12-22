FILE_PATH = './input.txt'


def input_to_elves(file_path):
    elves = []
    with open(file_path) as file:
        elf = []
        for line in file:
            line = line.strip()
            if len(line) > 0:
                num = int(line)
                elf.append(num)
            else:
                elves.append(elf)
                elf = []
    return elves


def sum_elves(elves):
    return [sum(elf) for elf in elves]


def most_calories(elves):
    return max(elves)


def main():
    elves = input_to_elves(FILE_PATH)
    sums = sum_elves(elves)
    print('Most calories: %d' % most_calories(sums))


if __name__ == "__main__":
    main()
