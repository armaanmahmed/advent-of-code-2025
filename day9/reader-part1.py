# day 9 part 1 solution
# @author armaanmahmed

def parse_file(filename: str):
    pts : list[tuple[int, int]] = []
    with open(filename, 'r') as file:
        pts = [tuple(int(num) for num in line.strip().split(',')) for line in file]
    
    if not pts:
        return 0
    
    max_area = 0
    
    # find the maximum area over all rectangles
    for first_x, first_y in pts:
        for sec_x, sec_y in pts:
            max_area = max(max_area, (first_x - sec_x + 1) * (first_y - sec_y + 1))

    return max_area


if __name__=='__main__':
    result = parse_file('./input.txt')
    print(f'Largest area is {result}')