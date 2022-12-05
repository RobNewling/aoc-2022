class AssignmentPair:
    def __init__(self, section1, section2):
        self.section1 = self.expand_section(section1)
        self.section2 = self.expand_section(section2)

    def expand_section(self, section):
        start, stop = section.split('-')
        return [i for i in range(int(start), int(stop)+1)]

    def detect_subsets(self):
        # true if one list is fully a subset of the other
        if (set(self.section1).issubset(self.section2)
                or set(self.section2).issubset(self.section1)):
            return True
        else:
            return False

    def detect_overlap(self):
        # true if one list overlaps the other at all
        if set(self.section1).intersection(self.section2):
            return True
        else:
            return False


def process_input(filename):
    assignment_pairs = []
    with open(filename, 'r') as input_file:
        for line in input_file:
            # print((line.strip().split(',')))
            assignment_pairs.append(AssignmentPair(*line.strip().split(',')))

    count = 0
    for pair in assignment_pairs:
        if pair.detect_overlap():
            count += 1

    print(f'Total pairs: {count}')


if __name__ == '__main__':
    process_input('input.txt')
