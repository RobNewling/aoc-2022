

def process_input(filename):
    with open(filename, 'r') as input_file:
        elf_snack_temp_count = []
        elf_snack_sums = []
        for line in input_file:
            if line.strip().isnumeric():
                elf_snack_temp_count.append(int(line.strip()))
            else:
                elf_snack_sums.append(sum(elf_snack_temp_count))
                elf_snack_temp_count.clear()

        max_calories = 0
        for num in range(1, 4):

            max_calories += max(elf_snack_sums)
            elf_number = elf_snack_sums.index(max(elf_snack_sums))
            print('Max Calories: ' + str(max(elf_snack_sums)))
            print('Elf #: ' + str(elf_number))
            del elf_snack_sums[elf_number]

        print('Max Calories: ' + str(max_calories))


if __name__ == '__main__':
    process_input('input.txt')
