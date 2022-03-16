from aiscpy.core import queryingToDB, queryToDict

def test_init_queryingToDB():
    A = queryingToDB('''
                         SELECT A FROM `W-M-S-HP_shapes_AISC`
                         WHERE Shape= 'W44X335'
                         ''')
    assert A.listQuery == [(98.5,)]
    assert queryToDict(A) ==[]