'''
clase para diseño de elementos de estructuras metalicas.
'''
from aiscpy.core import selectTable

def queryForSelect() -> str:
    str1 = "SELECT 'Shape' "
class SelectByCriteria():
    def __init__(self, typeShape: str, prop: str, criteria: float|int, typeCriteria = 'min') -> None:
        
        if not isinstance(typeShape, str):
            raise TypeError('typeShape must be a string')
        if not isinstance(prop, str):
            raise TypeError ('property name must be a string, example: "Sx" ')
        if not isinstance(criteria, (int, float)):
            raise TypeError('Criteria must be a number')
        if (typeCriteria != 'min' or typeCriteria != 'max' or typeCriteria != 'equal'):
            raise ValueError('typeCriteria must be a string in ["max", "min", "equal"]')
        
        self.__typeShape :str = typeShape
        self.__prop = prop
        self.__criteria = criteria
        self.__typeCriteria =  typeCriteria
        
        self.__table: str = selectTable(self.__typeShape)
        
        if self.__criteria == 'min':
            pass
        elif self.__criteria == 'max':
            pass
        elif self.__criteria == 'equal':
            pass
        else:
            raise ValueError('typeCriteria must be a string in ["max", "min", "equal"]')
        
    