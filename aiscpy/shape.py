import sqlite3
from aiscpy.core import queryToDict, queryingToDB

class Shape():
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__query = queryingToDB('''
                         SELECT * FROM `W-M-S-HP_shapes_AISC`
                         WHERE Shape= 'W44X335'
                         ''')
    
    def query(self):
        return self.__query
        
        
        

con = sqlite3.connect('aiscpy/DataBases/shapes_AISC.db')
cur = con.cursor()

shape_list = cur.execute('''
                         SELECT * FROM `W-M-S-HP_shapes_AISC`
                         WHERE Shape= 'W44X335'
                         ''')

col_name_list = [tuple[0] for tuple in shape_list.description]

lista = []
j = 0
for i in shape_list.fetchone(): 
    lista.append(i)
    
resultado = dict(zip(col_name_list, lista))
print(resultado)
con.close()