from utils.id_range import IDRange
from typing import List

def combine_ranges(ranges: List[IDRange]) -> List[IDRange]:
    currIdx = 0
    nextIdx = 1
    combined: List[IDRange] = []
    while nextIdx < len(ranges):
        currRange = ranges[currIdx]
        nextRange = ranges[nextIdx]
        if (nextRange.start <= currRange.end):
            currRange.end = max(currRange.end, nextRange.end)
            nextIdx += 1
        elif (nextRange.start > currRange.end):
            combined.append(currRange)
            currIdx = nextIdx
            nextIdx += 1
    combined.append(ranges[currIdx])
    return combined