from utils.rotation import Direction

def perform_rotation(position, direction, value) -> tuple[int, int]:
    """Determine final lock position, and count the number of times the dial passes 0"""
    
    # Count full rotations, and simplify the value so it is between 0 and 99
    zero_passes = value // 100
    value %= 100

    if direction == Direction.LEFT:
        value *= -1

    raw_position = position + value
    if ((raw_position <= 0 and position != 0) or raw_position >= 100):
        zero_passes += 1

    position = raw_position % 100
    return position, zero_passes