# day 1 part 2 solution
# @author armaanmahmed

def parse_file(filename: str):
    # initial position is 50, number of zeroes is 0
    pos = 50
    zero_count = 0
    LOCK_SIZE = 100

    with open(filename, 'r') as file:
        for line in file:
            old_pos = pos
            
            # parse second two digits as positive shift if R, otherwise L
            shift = int(line[1:]) if line[0] == 'R' else -int(line[1:])
            pos += shift

            # integer division accounts for extra shift in negative case
            cycles = abs(pos // LOCK_SIZE)
            rem = pos % LOCK_SIZE

            # handle landing on/getting off zeroes
            if pos <= 0:
                if rem == 0 and old_pos != 0:
                    cycles += 1
                elif rem != 0 and old_pos == 0:
                    cycles -= 1
            
            zero_count += cycles
            pos = rem
    
    return zero_count

if __name__=='__main__':
    file_zero_count = parse_file('./input.txt')
    print(f'Number of zeroes during or after a rotation: {file_zero_count}')
    