# day 11 part 2 solution
# @author armaanmahmed

from collections import defaultdict

def parse_file(filename: str):
    # build a graph as an adjacency list
    graph = defaultdict(list)

    with open(filename, 'r') as file:
        for line in file:
            tokens = [token.strip(':') for token in line.split()]
            graph[tokens[0]].extend(tokens[1:])
    
    num_vertices = len(graph)
    # after using BFS from part 1, we find that the given graph is acyclic
    # thus, there is no need to keep track of nodes visited and we can use dynamic programming

    # number of paths from node: dp[node][visited_dac][visited_fft]
    dp = defaultdict(lambda: [[-1, -1] for _ in range(2)])

    def dfs_visit(visited_dac, visited_fft, node):
        if node == 'out':
            return 1 if visited_dac and visited_fft else 0
        
        counted_paths = dp[node][visited_dac][visited_fft]
        if counted_paths != -1:
            return counted_paths
        
        count = 0
        for child in graph[node]:
            count += dfs_visit(visited_dac or child == 'dac', visited_fft or child == 'fft', child)
        
        dp[node][visited_dac][visited_fft] = count
        return count    
    
    return dfs_visit(False, False, 'svr')

if __name__=='__main__':
    result = parse_file('./input.txt')
    print(f'There are {result} paths from svr to out')