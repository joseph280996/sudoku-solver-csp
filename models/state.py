from typing import Dict, Tuple, List

from .Variable import Variable


class State:
    """
    This class represent a state in the Constraint Satisfaction Problem
    Properties:
        state: The current states of the variable
    """
    def __init__(self, state: Dict[Tuple[int, int], Variable]):
        self.state = state

    def next_state(self, coordinate: Tuple[int, int], new_domain: List[int]) -> "State":
        """
        This method will take in an assignment value for a variable and set its domain.
        This will cause cascading forward checking which will generate a whole new next state of the search space.
        Arguments:
            var_id: the coordinate on the sudoku grid for next assignment
            new_domain: domain with only 1 value to assign for that coordinate
        """
        copied_state = {}
        for key in self.state:
            copied_state[key] = self.state[key].copy()
        
        copied_state[coordinate].domain = new_domain

        # Inference
        self.__forward_checking(copied_state[coordinate].constraints, new_domain[0], copied_state)
        return State(copied_state)


    def __forward_checking(
        self,
        constraints: List[Tuple[int, int]],
        val: int,
        state: Dict[Tuple[int, int], Variable],
    ):
        """
        Forward checking by removing the values from the domain of the constraints 
        Arguments:
            constraints: The list of constraints of the current variable
            val: The value that was assign to the variable to remove from domain of constraints
            state: The current state of all the variables
        """
        for constraint in constraints:
            if val in state[constraint].domain:
                state[constraint].domain.remove(val)
