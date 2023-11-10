from functools import wraps
from typing import Tuple, Dict, List


class CSP:
    def __init__(self, csp):
        self.csp = csp


    def search(self) -> Dict[Tuple[int, int], int]:
        return self.__backtracking({})

    def __select_unassigned_var(self):
        raise NotImplemented
    
    def __order_domain_value(self) -> List[int]:
        raise NotImplemented

    def __is_consistent(self, val: int) -> bool:
        raise NotImplemented

    def __backtracking(self, assignments: Dict[Tuple[int, int], int]) -> Dict[Tuple[int, int], int]:
        if len(assignments) == len(self.csp):
            return assignments

        var = self.__select_unassigned_var()
        for val in self.__order_domain_value():
            if self.__is_consistent(val):
                assignments[var.id] = val

                result = self.__backtracking(assignments)

                if result:
                    return result
                
                del assignments[var.id]

        return {}


