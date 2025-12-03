def compare_segments(segments):
    for seg in segments:
        if seg != segments[-1]:
            return False
    return True