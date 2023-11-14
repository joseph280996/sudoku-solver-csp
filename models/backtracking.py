from collections import defaultdict
from typing import Tuple, Dict, List

from .state import State

from .variable import Variable


class BackTrackingSearch:
    """
    This class represent the Constraint Satisfaction Problem search algorithm.
    """

    def search(self, initial_state: State) -> Dict[Tuple[int, int], int] | None:
        """
        This method will search through all the domains and variables and see if there're any solution reached.
        It will preprocessing the variables' domain using arc-consistency AC3 algorithm to prune out the illegal possible assignments.
        If the solution is not reached after the prune, it will perform backtracking search on the search space.
        Arguments:
            csp: The list of variables of the problem
        Return:
            A list of assignments and its location of the assignment
        """
        self.__ac3(initial_state)
        if all(len(variable.domain) == 1 for variable in initial_state.state.values()):
            assignments = {}
            for variable in initial_state.state.values():
                assignments[variable.id] = variable.domain[0]
            return assignments

        return self.__backtracking_search({}, initial_state)

    def __backtracking_search(
        self, assignments: Dict[Tuple[int, int], int], curr_state: State
    ) -> Dict[Tuple[int, int], int] | None:
        """
        Backtracking search the variables to find solution
        Arguments:
            assignments: The assignments that we've made so far
            curr_state: The curr_state of the variables
        Returns:
            The assignments for each variable
        """
        # If we finished assigning all variables
        if len(assignments) == len(curr_state.state):
            return assignments

        # Select unassigned variable
        var = self.__select_unassigned_var(assignments, curr_state)

        # Select domain value after Ordering
        for val in self.__order_domain_value(var, curr_state):
            # if value is consistent
            if self.__is_consistent(var, val, assignments):
                next_state = curr_state.next_state(var.id, [val])
                # Assignment
                assignments[var.id] = val

                # Backtracking
                result = self.__backtracking_search(assignments, next_state)

                if result:
                    return result

                del assignments[var.id]

        return None

    def __select_unassigned_var(
        self, assignments: Dict[Tuple[int, int], int], curr_state: State
    ) -> Variable:
        """
        Select the variable with the least amount of domain to assign
        Arguments:
            assignments: The assignments that we have made so far
            curr_state: The current state of the variables
        Returns:
            The selected variable for assignment
        """
        unassigned_vars = [
            var for var in curr_state.state.values() if var.id not in assignments
        ]
        return min(unassigned_vars, key=lambda x: len(x.domain))

    def __order_domain_value(self, var: Variable, curr_state: State) -> List[int]:
        """
        Rank the domain of the current variable for assignment based on the number of neighbors that have the value in the domain or least constraining value.
        Arguments:
            var: The selected variable for assignment
            curr_state: The current state of the variables
        Returns:
            The ordered list of domain values
        """
        domain = var.domain
        if len(domain) == 1:
            return domain

        count = defaultdict(int)
        for val in domain:
            for constraint in var.constraints:
                if val in curr_state.state[constraint].domain:
                    count[val] += 1

        return sorted(count.keys(), key=lambda x: count.get(x))  # type: ignore

    def __is_consistent(
        self, var: Variable, val: int, assignments: Dict[Tuple[int, int], int]
    ) -> bool:
        """
        Check whether a given value of the domain is consistent with the variable constraints.
        Arguments:
            var: The selected variable for assignment
            val: The candidate value for assignment
            assignments: The assignments that we've made so far.
        Returns:
            A boolean indicates whether the value is consistent
        """
        for constraint_var in var.constraints:
            if constraint_var in assignments and assignments[constraint_var] == val:
                return False
        return True


    def __ac3(self, initial_state: State) -> None:
        """
        Arc-consistency check for pre-processing of the variables
        Arguments:
            initial_state: The initial state of the variable
        """
        arcs: List[Tuple[Tuple[int, int], Tuple[int, int]]] = [
            (coord, constraint)
            for coord in initial_state.state
            for constraint in initial_state.state[coord].constraints
        ]

        while len(arcs) > 0:
            arc = arcs.pop(0)
            if self.__remove__inconsistent_values(arc, initial_state):
                arcs = arcs + [
                    (constraint, arc[0])
                    for constraint in initial_state.state[arc[0]].constraints
                ]

    def __remove__inconsistent_values(
        self, arc: Tuple[Tuple[int, int], Tuple[int, int]], initial_state: State
    ):
        removed = False
        x_i, x_j = initial_state.state[arc[0]], initial_state.state[arc[1]]
        for x in x_i.domain:
            if len(x_j.domain) == 1 and x_j.domain[0] == x:
                x_i.domain.remove(x)
                removed = True
        return removed
