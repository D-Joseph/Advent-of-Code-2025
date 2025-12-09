from typing import List, Tuple
from utils.box import Box
import heapq

def build_distance_heap(boxes: List[Box], connections: int) -> List[Tuple[float, Box, Box]]:
    heap: List[Tuple[float, Box, Box]] = []
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            distance = boxes[i].calculate_distance(boxes[j]) * -1
            new_element = (distance, boxes[i], boxes[j])
            if len(heap) < connections: 
                  heapq.heappush(heap, new_element)
            elif len(heap) == connections and distance < heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, new_element)
    return heap