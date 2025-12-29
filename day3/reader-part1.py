# day 3 part 1 solution
# @author armaanmahmed

def parse_file(filename: str):
    total_joltage = 0
    with open(filename, 'r') as file:
        for bank in file:
            # initial/default value for the max digit
            max_dig = -1

            # initial/default values for the highest digits before/after max
            pre_max_dig, post_max_dig = -1, -1
            
            # convert each character to a digit
            for digit in (int(char) for char in bank.strip()):
                if digit > max_dig:
                    pre_max_dig = max_dig
                    max_dig = digit
                    post_max_dig = -1
                elif digit >= post_max_dig:
                    post_max_dig = digit
            
            # construct the number using the digits
            first, second = (pre_max_dig, max_dig) if post_max_dig == -1 else (max_dig, post_max_dig)
            total_joltage += 10 * first + second

    return total_joltage

if __name__=='__main__':
    result = parse_file('./input.txt')
    print(f'Total joltage is {result}')