# day 7 part 1 solution
# @author armaanmahmed

def parse_file(filename: str):
    # count the number of times beams were split
    splits = 0

    with open(filename, 'r') as file:
        file_lines = (line.strip() for line in file)
        first_line = next(file_lines)

        # initialize the beams as a single beam starting at S
        beam_set = set([first_line.find('S')])
        field_dim = len(first_line)

        for line in file_lines:
            new_beam_set = beam_set.copy()
            for beam in beam_set:
                if line[beam] == '^':
                    splits += 1
                    new_beam_set.remove(beam)
                    
                    # add to set if within the field
                    if beam - 1 >= 0:
                        new_beam_set.add(beam - 1)
                    if beam + 1 < field_dim:
                        new_beam_set.add(beam + 1)
            
            beam_set = new_beam_set
    
    return splits


if __name__=='__main__':
    result = parse_file('./input.txt')
    print(f'There were {result} beam splits')