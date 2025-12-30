# day 7 part 2 solution
# @author armaanmahmed

# for initialization of beam numbers as 0
from collections import defaultdict

def parse_file(filename: str):
    # count the number of timelines
    timelines = 0

    with open(filename, 'r') as file:
        file_lines = (line.strip() for line in file)
        first_line = next(file_lines)
        field_dim = len(first_line)

        # maintain a map of how many timelines (i.e. beams) are at each position
        beam_numbers = defaultdict(int)

        # initialize the beams as a single beam starting at the S
        beam_numbers[first_line.find('S')] = 1

        for line in file_lines:
            new_beam_numbers = beam_numbers.copy()
            for beam in beam_numbers:
                if line[beam] == '^':
                    num_beams = beam_numbers[beam]

                    # no beams are possible at this position
                    new_beam_numbers[beam] = 0

                    # send beams left and right, if possible
                    if beam + 1 < field_dim:
                        new_beam_numbers[beam + 1] += num_beams
                    if beam - 1 >= 0:
                        new_beam_numbers[beam - 1] += num_beams
            
            beam_numbers = new_beam_numbers
        
        # sum the number of active timelines
        timelines += sum(beam_numbers.values())
    
    return timelines

if __name__=='__main__':
    result = parse_file('./input.txt')
    print(f'There were {result} different timelines')