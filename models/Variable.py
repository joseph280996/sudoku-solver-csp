from typing import List, Tuple


class Variable:
    constraints: List[Tuple[int, int]] = []

    def __init__(self, id: Tuple[int, int], domain: List[int]):
        self.id = id
        self.domain = domain
    
    def copy(self) -> "Variable":
        """
        Create a deep copy of the variable to keep the next state of the CSP tree isolate
        Returns:
            A new instance of variable that has all the copied properties of the current instance
        """
        domain_copy = list(self.domain)
        new_var = Variable(self.id, domain_copy)
        new_var.constraints = self.constraints

        return new_var
