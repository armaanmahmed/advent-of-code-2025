# day 2 part 1 solution
# @author armaanmahmed

def parse_file(filename: str):
    # running sum of invalid numbers
    sum = 0
    with open(filename, 'r') as file:
        # parse into list of lists of [lower_bound, upper_bound]
        range_list = [range_str.split('-') for range_str in file.read().split(',')]
        for lower, upper in range_list:
            # length of each bound in characters
            lower_bound = int(lower)
            upper_bound = int(upper)
            num = lower_bound
            
            while num <= upper_bound:
                num_str = str(num)
                num_len = len(num_str)
                
                # fast-forward odd-length ranges
                if num_len % 2 == 1:
                    num = pow(10, num_len)

                    # if out of bounds, move to the next range
                    if num > upper_bound:
                        break
                    num_len += 1
                    num_str = str(num)
                
                # guaranteed to be even-length here
                split_bound = num_len // 2
                half = num_str[:split_bound]
                
                # fast-forward asymmetrical numbers
                if half + half != num_str:
                    target = int(half + half)
                    if num <= target <= upper_bound:
                        num = target
                        num_str = str(num)
                    

                # check for symmetrical number
                if half + half == num_str:
                    sum += num
                
                # find next symmetrical number
                next_half = str(int(half) + 1)
                if len(half) > 0 and len(next_half) == len(half):
                    num = int(next_half + next_half)
                else:
                    num += 1

    return sum


if __name__=='__main__':
    result = parse_file('./input.txt')
    print(f'sum of invalid numbers is {result}')