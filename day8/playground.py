from utils.build_distance_heap import build_distance_heap
from utils.read_boxes import read_boxes

class PlaygroundSolver:
    def __init__(self, connections):
        self.boxes = read_boxes()
        self.heap = build_distance_heap(self.boxes, connections)

    def solve_part1(self):
        pass

if __name__ == '__main__':
    solver = PlaygroundSolver(10)
    print(solver.heap)
    print(len(solver.heap))