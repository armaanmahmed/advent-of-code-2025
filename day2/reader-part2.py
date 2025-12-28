# day 2 part 2 solution
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

            for num in range(lower_bound, upper_bound + 1):
                num_str = str(num)
                num_len = len(num_str)

                # only substrings with length dividing evenly are candidates
                for substr_size in range(1, num_len // 2 + 1):
                    cat_str = num_str[:substr_size] * (num_len // substr_size)
                    if cat_str == num_str:
                        sum += num
                        break
    return sum


if __name__=='__main__':
    result = parse_file('./input.txt')
    print(f'sum of invalid numbers is {result}')