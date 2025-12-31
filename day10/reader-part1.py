# day 10 part 1 solution
# @author armaanmahmed

def parse_file(filename: str):
    total_presses = 0
    with open(filename, 'r') as file:
        for line in file:
            tokens = line.split()

            indicator_lights = [char == '#' for char in tokens[0].strip('[]')]
            curr_state = [False] * len(indicator_lights)
            buttons = [[int(num) for num in tok.strip('()').split(',')] for tok in tokens[1:-1]]
            
            _, min_num_ops = explore(curr_state, [], indicator_lights, 0, buttons)
            
            total_presses += min_num_ops

    return total_presses

def explore(curr_state, applied_changes: list[int], target_state, curr_idx, buttons):
    min_num_ops = len(buttons) + 1
    ac_to_return = []

    for btn_idx in range(curr_idx, len(buttons)):
        button = buttons[btn_idx]

        applied_changes.append(btn_idx)

        for idx in button:
            curr_state[idx] = not curr_state[idx]
        
        # if target, mark current as successful
        if curr_state == target_state and len(applied_changes) < min_num_ops:
            min_num_ops = len(applied_changes)
            ac_to_return = applied_changes.copy()
        
        # check if recursive option is successful
        ac, ret_num_ops = explore(curr_state, applied_changes, target_state, btn_idx + 1, buttons)
        
        if ret_num_ops < min_num_ops:
            min_num_ops = ret_num_ops
            ac_to_return = ac
        
        # undo changes
        applied_changes.pop()
        for idx in button:
            curr_state[idx] = not curr_state[idx]
    
    return ac_to_return, min_num_ops


if __name__=='__main__':
    result = parse_file('./input.txt')
    print(f'It takes {result} total button presses')