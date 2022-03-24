from aiscpy.core import selectTable, strForSelect

def test_select_table():
    table1 = selectTable('W')
    table2 = selectTable('M')
    table3 = selectTable('S')
    table4 = selectTable('HP')
    table5 = selectTable('C')
    table6 = selectTable('MC')
    
    assert table1 == '`W-M-S-HP_shapes_AISC`'
    assert table2 == '`W-M-S-HP_shapes_AISC`'
    assert table3 == '`W-M-S-HP_shapes_AISC`'
    assert table4 == '`W-M-S-HP_shapes_AISC`'
    assert table5 == '`C-MC_shapes_AISC`'
    assert table6 == '`C-MC_shapes_AISC`'
    
def test_instruction():
    instruction1 = strForSelect(selectTable('W'), all=True)
    testing1 = "SELECT * FROM `W-M-S-HP_shapes_AISC` "
    
    instruction2 = strForSelect(selectTable('C'), name= 'A')
    testing2 = "SELECT 'A' FROM `C-MC_shapes_AISC` "
    
    assert instruction1 == testing1
    assert instruction2 == testing2