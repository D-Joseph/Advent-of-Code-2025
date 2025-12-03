class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __str__(self):
        return f'Start: {self.start}, End: {self.end}'