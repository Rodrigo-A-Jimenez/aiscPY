from aiscpy.design import SelectByCriteria


def test_select_by_criteria():
    s1 = SelectByCriteria('W', 'A', 35, 'min')
    assert s1.query.queryToList == ['W', 'W18X119', 35.1,  19,  0.655,  11.3,  1.06,  1.46,  1.9375,  1.1875,  15.125,  5.5,  119, 5.31,  24.5,  2190,  231,  7.9,  262,  253,  44.9,  2.69,  69.1,  3.13,  17.9,  10.6,  20300,  50.7,  152,  50.6,  131]
