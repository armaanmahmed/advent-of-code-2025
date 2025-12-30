# day 8 part 2 solution
# @author armaanmahmed

from math import sqrt
from collections import defaultdict

class UnionFind:
    def __init__(self):
        self.elem_map = {}
        self.ranks = defaultdict(int)
        self.num_sets = 0
    
    def make_set(self, elem):
        """
        Adds a set containing this element to the data structure.
        """
        if elem not in self.elem_map:
            self.num_sets += 1
        
        self.elem_map[elem] = elem
    
    def union(self, elem_one, elem_two):
        """
        Joins the set containing element one and element two.
        No effect if they are already within the same set.
        """
        first_rep = self.find(elem_one)
        second_rep = self.find(elem_two)

        if first_rep == second_rep:
            return
        
        # joining two existing sets so size decreases
        self.num_sets -= 1

        first_rank = self.elem_map[elem_one]
        second_rank = self.elem_map[elem_two]

        if first_rank < second_rank:
            self.elem_map[first_rep] = second_rep
        else:
            self.elem_map[second_rep] = first_rep
            if first_rank == second_rank:
                self.elem_map[first_rep] += 1

    def find(self, elem):
        current = elem

        # path compression
        if self.elem_map[current] != current:
            rep = self.find(self.elem_map[current])
            self.elem_map[current] = rep
            current = rep
        
        return current
    
    def to_sets(self):
        element_map = defaultdict(list)
        for element, _ in self.elem_map.items():
            rep = self.find(element)
            element_map[rep].append(element)
        
        return [(rep, children) for rep, children in element_map.items()]
    
    def size(self):
        return self.num_sets


def parse_file(filename: str):
    points : list[tuple[int, int, int]] = []
    with open(filename, 'r') as file:
        points = [tuple(int(num) for num in line.split(',')) for line in file]
    
    # generate all unique pairs of points
    point_pairs = []
    for p_first in range(len(points)):
        for p_second in range(p_first):
            point_pairs.append((points[p_first], points[p_second]))

    # computes the squared distance between a pair of points
    def get_dist(point_pair):
        first_point, second_point = point_pair
        squared_dist = sum(pow(first_point[dim] - second_point[dim], 2) for dim in range(3))
        return sqrt(squared_dist)
    
    if not point_pairs:
        return 1
    
    point_pairs.sort(key=get_dist)

    # make a set for all points
    point_sets = UnionFind()
    for point in points:
        point_sets.make_set(point)
    
    # break if only a single set remaining
    for point_one, point_two in point_pairs:
        point_sets.union(point_one, point_two)
        if point_sets.size() == 1:
            break
    
    return point_one[0] * point_two[0]


if __name__=='__main__':
    result = parse_file('./input.txt')
    print(f'Product of the x-coordinates is {result}')