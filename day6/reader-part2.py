# day 6 part 2 solution
# @author armaanmahmed

# for fast computation of products over an Iterable
from math import prod

# easier management of default dict values
from collections import defaultdict

def parse_file(filename: str):
    total_sum = 0
    with open(filename, 'r') as file:
        # list of numbers to combine
        raw_nums: list[tuple[int, str]] = []

        # list of operations to perform
        ops : list[str] = []
        max_len = -1

        for line in file:
            max_len = max(max_len, len(line))
            for char_idx, char in enumerate(line):
                if char == ' ' or char == '\n':
                    continue
                elif char == '+' or char == '*':
                    # last line
                    ops.append(char)
                else:
                    raw_nums.append((char_idx, char))
        
        # will not happen for given input file
        if not raw_nums:
            return 0

        # step 1: map indices to ordered list of digit characters
        processed_nums = defaultdict(list)
        for idx, num in raw_nums:
            processed_nums[idx].append(num)
        
        # step 2: map indices to numbers
        for idx, nums in processed_nums.items():
            processed_nums[idx] = int(''.join(nums))
        
        # index in the list of operations
        op_index = 0
        curr_nums = []

        for idx in range(max_len):
            if processed_nums[idx] == []:
                # the column has no digits; process the accumulation so far
                if ops[op_index] == '+':
                    total_sum += sum(curr_nums)
                else:
                    total_sum += prod(curr_nums)
                
                # move to the next operation and set of numbers
                curr_nums = []
                op_index += 1
            else:
                curr_nums.append(processed_nums[idx])
    
    return total_sum



if __name__=='__main__':
    result = parse_file('./input.txt')
    print(f'Total sum across all columns is {result}')