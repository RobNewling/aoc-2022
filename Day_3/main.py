class ElfGroup:
    def __init__(self, group_rucksacks):
        self.rucksacks = group_rucksacks

    def find_badge(self):
        return list(set(self.rucksacks[0].entire_inventory).intersection(self.rucksacks[1].entire_inventory, self.rucksacks[2].entire_inventory))[0]


class Rucksack:
    def __init__(self, total_item_list):
        self.entire_inventory = total_item_list
        self.compartment_a = [] # list of items
        self.compartment_b = [] # list of items
        self.divide_items_into_compartments(total_item_list)

    def divide_items_into_compartments(self, total_item_list):
        self.compartment_a = total_item_list[:len(total_item_list)//2]
        self.compartment_b = total_item_list[len(total_item_list)//2:]

    def find_item_appearing_in_both_compartments(self):
        return list(set(self.compartment_a).intersection(self.compartment_b))[0]


class Item:
    def __init__(self, type):
        self.type = type

    def priority(self):
        # ASCII A = 65, Z = 90, a = 97, z = 122
        if self.type.isupper():
            return ord(self.type)-38
        elif self.type.islower():
            return ord(self.type)-96
        else:
            print('Error. Invalid type.')


def process_input(filename):
    rucksacks = []
    item_priorities = []
    elf_groups_prep = []
    elf_groups = []

    # load rucksacks
    with open(filename, 'r') as input_file:
        for line in input_file:
            rucksacks.append(Rucksack(line.strip()))

    # form groups
    elf_groups_prep = [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]
    for group in elf_groups_prep:
        elf_groups.append(ElfGroup(group))

    # gather priorities
    for group in elf_groups:
        item = Item(group.find_badge())
        # print(f'Item {item.type} with priority {item.priority()}')
        item_priorities.append(item.priority())

    print(f'Sum of items: {sum(item_priorities)}')


if __name__ == '__main__':
    process_input('input.txt')
