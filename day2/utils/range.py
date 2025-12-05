class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return f'Start: {self.start}, End: {self.end}'

    def __repr__(self):
        return self.__str__()