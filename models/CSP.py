from collections import defaultdict
from typing import Tuple, Dict, List

from .variable import Variable


class CSP:
    """
    This class represent the Constraint Satisfaction Problem search algorithm.
    """
    def search(self, csp: Dict[Tuple[int, int], Variable]) -> Dict[Tuple[int, int], int] | None:
        """
        This method will search through all the domains and variables and see if there're any solution reached.
        It will preprocessing the variables' domain using arc-consistency AC3 algorithm to prune out the illegal possible assignments.
        If the solution is not reached after the prune, it will perform backtracking search on the search space.
        Arguments:
            csp: The list of variables of the problem
        Return:
            A list of assignments and its location of the assignment
        """
        self.__ac3(csp)
        if all(len(variable.domain) == 1 for variable in csp.values()):
            assignments = {}
            for variable in csp.values():
                assignments[variable.id] = variable.domain[0]
            return assignments

        return self.__backtracking_search({}, csp)

    def __backtracking_search(self, assignments: Dict[Tuple[int, int], int], csp: Dict[Tuple[int, int], Variable]) -> Dict[Tuple[int, int], int] | None:
        # If we finished assigning all variables
        if len(assignments) == len(csp):
            return assignments

        # Select unassigned variable
        var = self.__select_unassigned_var(assignments, csp)

        # Select domain value after Ordering
        for val in self.__order_domain_value(var, csp):
            # if value is consistent
            if self.__is_consistent(var, val, assignments):
                csp_copy = self.__deep_copy_variables(csp)
                # Assignment
                assignments[var.id] = val
                csp_copy[var.id].domain = [val]

                # Inference
                self.__forward_checking(csp_copy[var.id].constraints, val, csp_copy)

                # Backtracking
                result = self.__backtracking_search(assignments, csp_copy)

                if result:
                    return result
                
                del assignments[var.id]

        return None
    
    def __deep_copy_variables(self, csp: Dict[Tuple[int, int], Variable]) -> Dict[Tuple[int, int], Variable]:
        new_dict = {}
        for key in csp:
            new_dict[key] = csp[key].copy()
        
        return new_dict

    def __select_unassigned_var(self, assignments: Dict[Tuple[int, int], int], csp: Dict[Tuple[int, int], Variable]) -> Variable:
        unassigned_vars = [var for var in csp.values() if var.id not in assignments]
        return min(unassigned_vars, key = lambda x: len(x.domain))
    
    def __order_domain_value(self, var: Variable, csp: Dict[Tuple[int, int], Variable]) -> List[int]:
        domain = var.domain
        if len(domain) == 1:
            return domain

        count = defaultdict(int)
        for val in domain:
            for constraint in var.constraints:
                if val in csp[constraint].domain:
                    count[val] += 1
        
        return sorted(count.keys(), key = lambda x: count.get(x)) # type: ignore

    def __is_consistent(self, var:Variable, val: int, assignments: Dict[Tuple[int, int], int]) -> bool:
        for constraint_var in var.constraints:
            if constraint_var in assignments and assignments[constraint_var] == val:
                return False
        return True
    

    def __forward_checking(self, constraints: List[Tuple[int, int]], val: int, csp: Dict[Tuple[int, int], Variable]):
        for constraint in constraints:
            if val in csp[constraint].domain:
                csp[constraint].domain.remove(val)

    def __ac3(self, csp: Dict[Tuple[int, int], Variable]):
        arcs: List[Tuple[Tuple[int, int], Tuple[int, int]]] = [(coord, constraint) for coord in csp for constraint in csp[coord].constraints]

        while len(arcs) > 0:
            arc = arcs.pop(0)
            if self.__remove__inconsistent_values(arc, csp):
                arcs = arcs + [(constraint, arc[0]) for constraint in csp[arc[0]].constraints]

    def __remove__inconsistent_values(self, arc: Tuple[Tuple[int, int], Tuple[int, int]], csp: Dict[Tuple[int, int], Variable]):
        removed = False
        x_i, x_j = csp[arc[0]], csp[arc[1]]
        for x in x_i.domain:
            if len(x_j.domain) == 1 and x_j.domain[0] == x:
                x_i.domain.remove(x)
                removed = True
        return removed
