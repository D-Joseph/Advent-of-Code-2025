class IDRange:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end
    
    def __str__(self) -> str:
        return f'{self.start} -> {self.end}'
    
    def __repr__(self) -> str:
        return self.__str__()