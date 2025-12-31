# day 9 part 2 solution
# @author armaanmahmed

def parse_file(filename: str):
    pts : list[tuple[int, int]] = []
    with open(filename, 'r') as file:
        pts = [tuple(int(num) for num in line.strip().split(',')) for line in file]

    if not pts:
        return 0
    
    edges, areas = [], []
    num_pts = len(pts)
    
    # get area from rectangles
    def get_area(x_one, y_one, x_two, y_two):
        return (abs(x_two - x_one) + 1) * (abs(y_two - y_one) + 1)
    
    for idx in range(num_pts):
        edges.append(sorted((pts[idx], pts[idx-1])))
        for s_idx in range(idx + 1, num_pts):
            pt_one, pt_two = sorted((pts[idx], pts[s_idx]))
            areas.append((get_area(*pt_one, *pt_two), pt_one, pt_two))

    areas.sort(reverse=True)

    for area, (x_one, y_one), (x_two, y_two) in areas:
        y_one, y_two = sorted((y_one, y_two))
        # left to right, bottom to top; check for any intersection at all
        if not any(
                (o_x_two > x_one and o_x_one < x_two and o_y_two > y_one and o_y_one < y_two) 
                for (o_x_one, o_y_one), (o_x_two, o_y_two) in edges
            ):
            return area
    
    return 0

if __name__=='__main__':
    result = parse_file('./input.txt')
    print(f'result is {result}')