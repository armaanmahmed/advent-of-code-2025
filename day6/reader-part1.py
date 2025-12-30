# day 6 part 1 solution
# @author armaanmahmed

# for fast computation of products over an Iterable
from math import prod

def parse_file(filename: str):
    total_sum = 0
    with open(filename, 'r') as file:
        # list of lists of numbers to combine
        nums = []

        # list of operations to perform
        ops = []

        for line_num, line in enumerate(file):
            tokens = line.split()

            if line_num == 0:
                nums = [[int(token)] for token in tokens]
                continue

            if '+' in tokens or '*' in tokens:
                ops = tokens
                break
        
            for idx, token in enumerate(tokens):
                nums[idx].append(int(token))

        for idx, op in enumerate(ops):
            if op == '+':
                total_sum += sum(nums[idx])
            else:
                total_sum += prod(nums[idx])
    
    return total_sum



if __name__=='__main__':
    result = parse_file('./input.txt')
    print(f'Total sum across all columns is {result}')