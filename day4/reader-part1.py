# day 4 part 1 solution
# @author armaanmahmed

def parse_file(filename: str):
    reachable = 0
    with open(filename, 'r') as file:
        maze = [row.strip() for row in file]
        num_rows, num_cols = len(maze), len(maze[0])

        # get the neighbors of a given cell
        NEIGHBORS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        # iterate through each position and inspect those that have a roll
        for row in range(num_rows):
            for col in range(num_cols):
                if maze[row][col] == '.':
                    continue

                # check this positions neighbors, if they are in bounds
                num_neighbors = 0
                for y_shift, x_shift in NEIGHBORS:
                    y, x = row + y_shift, col + x_shift
                    if 0 <= y < num_rows and 0 <= x < num_cols:
                        if maze[y][x] == '@':
                            num_neighbors += 1
                
                # if less than four neighbors that are rolls, the roll is reachable
                if num_neighbors < 4:
                    reachable += 1
    
    return reachable

if __name__=='__main__':
    result = parse_file('./input.txt')
    print(f'There are {result} reachable rolls')