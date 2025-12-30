# day 8 part 1 solution
# @author armaanmahmed

from math import sqrt
from collections import defaultdict

class UnionFind:
    def __init__(self):
        self.elem_map = {}
        self.ranks = defaultdict(int)
    
    def make_set(self, elem):
        """
        Adds a set containing this element to the data structure.
        """
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


def parse_file(filename: str, k: int):
    set_size_prod = 1
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
    
    point_pairs.sort(key=get_dist)

    # find the k closest pairs of points
    closest_pairs = point_pairs[:k]

    # will only be calling union on the pairs of closest points; only need sets for those
    point_sets = UnionFind()
    for point_one, point_two in closest_pairs:
        point_sets.make_set(point_one)
        point_sets.make_set(point_two)
    
    for point_one, point_two in closest_pairs:
        point_sets.union(point_one, point_two)
    
    # sort by the size of the sets, descending
    sets = point_sets.to_sets()
    sets.sort(key=lambda tup: len(tup[1]), reverse=True)


    # return the product of the sizes of the largest three sets
    for point, children in sets[:3]:
        set_size_prod *= len(children)
    
    return set_size_prod



if __name__=='__main__':
    result = parse_file('./input.txt', 1000)
    print(f'result is {result}')