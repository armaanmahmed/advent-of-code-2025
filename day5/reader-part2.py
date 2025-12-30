# day 5 part 2 solution
# @author armaanmahmed

def parse_file(filename: str):
    ranges = []

    with open(filename, 'r') as file:
        # process all ranges
        for interval in file:
            interval = interval.strip()
            if interval == '':
                break
            ranges.append([int(num) for num in interval.split('-')])
    
    # will not happen for given input file
    if not ranges:
        return 0
    
    # sort by start time
    ranges.sort(key=lambda x: x[0])

    # merge into disjoint intervals
    curr_start, curr_end = ranges[0]
    merged_ranges = []

    for start, end in ranges:
        # overlapping interval; extend current
        if start <= curr_end:
            curr_end = max(curr_end, end)
        else:
            # disjoint interval; start a new interval
            merged_ranges.append((curr_start, curr_end))
            curr_start, curr_end = start, end
    
    merged_ranges.append((curr_start, curr_end))

    # return the sum of sizes of each interval
    return sum(end - start + 1 for start, end in merged_ranges)


if __name__=='__main__':
    result = parse_file('./input.txt')
    print(f'There are {result} fresh ingredients')