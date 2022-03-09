import sqlite3 

con = sqlite3.connect('aiscpy/DataBases/shapes_AISC.db')
cur = con.cursor()
cons = cur.execute(
    '''
    SELECT Shape FROM `W-M-S-HP_shapes_AISC`
    WHERE A BETWEEN 95 AND 100
    '''
)
lista = []
for i in cons:
    lista.append(i[0])

print(lista)


'''for i in range(len(lista)):
    print(lista[i][0])'''
con.commit()
con.close()