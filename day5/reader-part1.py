# day 5 part 1 solution
# @author armaanmahmed

def parse_file(filename: str):
    fresh = 0
    with open(filename, 'r') as file:
        file_lines = (line.strip() for line in file)
        ranges = []
        
        # process all ranges
        for interval in file_lines:
            if interval == '':
                break
            ranges.append([int(num) for num in interval.split('-')])
        
        # sort by start time
        ranges.sort(key=lambda x: x[0])

        # generator maintains state; resumes from next line
        ids = [int(id) for id in file_lines]

        for id in ids:
            for start, end in ranges:
                # range list is sorted so no more intervals can match
                if id < start:
                    break
                if id <= end:
                    fresh += 1
                    break
    
    return fresh


if __name__=='__main__':
    result = parse_file('./input.txt')
    print(f'There are {result} fresh ingredients')