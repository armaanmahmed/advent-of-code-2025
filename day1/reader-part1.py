# day 1 part 1 solution
# @author armaanmahmed

def parse_file(filename: str):
    # initial position is 50, number of zeroes is 0
    pos = 50
    zero_count = 0
    LOCK_SIZE = 100

    with open(filename, 'r') as file:
        for line in file:
            shift = int(line[1:]) if line[0] == 'R' else -int(line[1:])
            pos += shift
            
            if pos % LOCK_SIZE == 0:
                zero_count += 1
    return zero_count

if __name__=='__main__':
    file_zero_count = parse_file('./input.txt')
    print(f'Number of zeroes after a rotation: {file_zero_count}')
    