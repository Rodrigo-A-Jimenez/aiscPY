'''
clase para diseño de elementos de estructuras metalicas.
'''
def criteria(list: list):
    pass


class SelectByCriteria():
    def __init__(self, typeShape: str, prop: str, propCriteria: list|int|float) -> None:
        if not isinstance(typeShape, str):
            raise TypeError('typeShape must be a string')
        if not isinstance(prop, str):
            raise TypeError('char or characteristic must be a string, example: "Sx" ')
        if not isinstance(propCriteria, (list, int, float)):
            raise TypeError('Criteria must be a number, or list of number, [min: float, max: float]')
        
        self.__typeShape = typeShape
        self.__prop = prop
        self.__propCriteria = propCriteria
        
        if isinstance(self.__propCriteria, list):
            if len(self.__propCriteria) != 2:
                raise ValueError('List must be a list with two elements')
            self.__minCriteria = self.__propCriteria[0]
            self.__maxCriteria = self.__propCriteria[1]
        else:
             self.__minCriteria = self.__propCriteria
             self.__maxCriteria = self.__propCriteria