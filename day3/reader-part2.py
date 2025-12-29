# day 3 part 2 solution
# @author armaanmahmed

def parse_file(filename: str):
    total_joltage = 0
    with open(filename, 'r') as file:
        for bank in file:
            # queue of digits currently processed
            dig_queue = []
            for digit in bank:
                if len(dig_queue) < 12:
                    dig_queue.append(digit)
                else:
                    num_str = ''.join(dig_queue)
                    for idx in range(12):
                        candidate = num_str[:idx] + num_str[idx + 1:] + digit
                        # add if the resultant number would be larger than current
                        if int(candidate) > int(num_str):
                            dig_queue.pop(idx)
                            dig_queue.append(digit)
                            break
            # add the number resulting from joining on the digit queue 
            total_joltage += int(''.join(dig_queue))
                        
    return total_joltage

if __name__=='__main__':
    result = parse_file('./input.txt')
    print(f'Total joltage is {result}')