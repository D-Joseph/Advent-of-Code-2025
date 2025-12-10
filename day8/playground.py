import heapq
from typing import Dict, List
from utils.build_distance_heap import build_distance_heap
from utils.read_boxes import read_boxes
from utils.box import Box


class PlaygroundSolver:
    def __init__(self, connections):
        self.boxes = read_boxes()
        self.heap = build_distance_heap(self.boxes, connections)
        

    def solve_part1(self):
        heap = self.heap
        lookupBoxCircuit: Dict[Box, set] = {} 
        sets:List[set[Box]] = []
        _, b1, b2 = heapq.heappop(heap)
        while heap:
            # Case 1: No elements in lookupBoxCircuit
                # Create a new set that represents the new circuit
                # Register these Box <-> Set connection
            if b1 not in lookupBoxCircuit and b2 not in lookupBoxCircuit:
                newSet = set([b1, b2])
                sets.append(newSet)
                lookupBoxCircuit[b1] = newSet
                lookupBoxCircuit[b2] = newSet
            # Case 2: Both elements in lookupBoxCircuit
                # Need to connect both of the circuits together and update references
                    # Combine both sets together
                    # Update all boxes in either set to reference new Set 
                    # Remove old sets from list
            elif b1 in lookupBoxCircuit and b2 in lookupBoxCircuit and lookupBoxCircuit[b1] != lookupBoxCircuit[b2]:
                oldB1Set = lookupBoxCircuit[b1]
                oldB2Set = lookupBoxCircuit[b2]
                newSet = oldB1Set | oldB2Set
                for box in newSet:
                    lookupBoxCircuit[box] = newSet
                sets.remove(oldB1Set)
                sets.remove(oldB2Set)
                sets.append(newSet)
                
            # Case 3: One element in lookupBoxCircuit
                # Add other element to set
                # Register in Box <-> Set
            elif b1 not in lookupBoxCircuit or b2 not in lookupBoxCircuit:
                isB1inCircuit = b1 in lookupBoxCircuit

                inCircuit, notInCircuit = (b1, b2) if isB1inCircuit else (b2, b1)
                lookupBoxCircuit[inCircuit].add(notInCircuit)
                lookupBoxCircuit[notInCircuit] = lookupBoxCircuit[inCircuit]
            _, b1, b2 = heapq.heappop(heap)

        return lookupBoxCircuit, sets

if __name__ == '__main__':
    solver = PlaygroundSolver(10)
    p1 = solver.solve_part1()
    for s in p1[1]:
        print(s)