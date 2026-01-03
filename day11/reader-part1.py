# day 11 part 1 solution
# @author armaanmahmed

from collections import defaultdict

def parse_file(filename: str):
    # build a graph as an adjacency list
    graph = defaultdict(list)
    visited = defaultdict(bool)
    num_paths = 0

    with open(filename, 'r') as file:
        for line in file:
            tokens = [token.strip(':') for token in line.split()]
            graph[tokens[0]].extend(tokens[1:])
    
    exploring = graph['you']
    
    # breadth-first search
    while exploring:
        curr_node = exploring.pop(0)
        if curr_node == 'out':
            num_paths += 1
            continue

        visited[curr_node] = True
        exploring.extend([node for node in graph[curr_node] if not visited[node]])
    
    return num_paths

if __name__=='__main__':
    result = parse_file('./input.txt')
    print(f'There are {result} paths from you to out')