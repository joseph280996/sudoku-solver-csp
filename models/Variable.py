from typing import List, Tuple


class Variable:
    constraints: List["Variable"]
    def __init__(
            self,
            id: Tuple[int, int],
            domain: List[int]):
        self.id = id
        self.domain = domain


