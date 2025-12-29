# day 4 part 2 solution
# @author armaanmahmed

def parse_file(filename: str):
    reachable = 0
    with open(filename, 'r') as file:
        maze = [[char for char in row.strip()] for row in file]
        num_rows, num_cols = len(maze), len(maze[0])

        # get the neighbors of a given cell
        NEIGHBORS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        # initialize visit list
        to_visit = [(row, col) for col in range(num_cols) for row in range(num_rows) if maze[row][col] == '@']

        while to_visit:
            row, col = to_visit.pop()

            # skip if this position does not have a roll
            if maze[row][col] == '.':
                continue

            # check this position's neighbors
            neighbor_rolls = []
            for y_shift, x_shift in NEIGHBORS:
                y, x = row + y_shift, col + x_shift

                # if in bounds and a roll, add to neighbor rolls
                if 0 <= y < num_rows and 0 <= x < num_cols:
                    if maze[y][x] == '@':
                        neighbor_rolls.append((y, x))

            if len(neighbor_rolls) < 4:
                # free the space and check the neighbors
                maze[row][col] = '.'
                reachable += 1
                to_visit.extend(neighbor_rolls)
    
    return reachable

if __name__=='__main__':
    result = parse_file('./input.txt')
    print(f'There are {result} recursively reachable rolls')