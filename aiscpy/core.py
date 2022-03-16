import sqlite3

class queryingToDB():
    def __init__(self, query: str, fetchone:bool = False) -> None:
        if not isinstance(fetchone, bool):
            raise TypeError('"fetchone" not in a bool')
        
        self.__fetchoneStatus = fetchone
        
        con = sqlite3.connect('aiscpy/DataBases/shapes_AISC.db')
        cur = con.cursor()
        self.__query_execute = cur.execute(query)
        self.__keysQuery = [tuple[0] for tuple in self.__query_execute.description]
        
        if(fetchone):
            self.__query_list = list(self.__query_execute.fetchone())
        else:
            self.__query_list = list(self.__query_execute.fetchall())
            
        
        con.close()
    
    @property
    def query(self):
        return self.__query_execute
    
    @property
    def queryToList(self):
        return self.__query_list
    
    @property
    def fetchoneStatus(self):
        return self.__fetchoneStatus
    
    @property
    def keysQuery(self):
        return self.__keysQuery
    
    def toDict(self):
        if (self.__fetchoneStatus):
            return dict(zip(self.__keysQuery, self.__query_list))
        else:
            raise ValueError('"fetchoneStatus" is False, not supported')
