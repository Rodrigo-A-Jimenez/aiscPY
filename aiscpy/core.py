import sqlite3

def queryToDict(query):
    keys_q = [tuple[0] for tuple in query.description]
    values_q = list(query.fetchone)
    return toDict(keys_q, values_q)

def toDict(keys: list | str, values: list) -> dict:
    """Query selection to dictionary of values, 

    Args:
        keys (list | str): Keys's list
        values (list): values's list

    Returns:
        dict: dictionary{'key': value}
    """    
    return dict(zip(keys, values))

class queryingToDB():
    def __init__(self, query: str) -> None:
        con = sqlite3.connect('aiscpy/DataBases/shapes_AISC.db')
        cur = con.cursor()
        self.__query_execute = cur.execute(query)
        self.__listQuery = self.__query_execute.fetchall()
        con.close()
    
    @property
    def query(self):
        return self.__query_execute
    
    @property
    def listQuery(self):
        return self.__listQuery
    