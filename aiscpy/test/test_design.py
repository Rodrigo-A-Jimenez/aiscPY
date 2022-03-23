from aiscpy.design import SelectByCriteria


def test_select_by_criteria_props():
    S1 = SelectByCriteria('W', 'Sx', [25, 30])
    S2 = SelectByCriteria('C', 'Sy', 50)
    
    assert S1.maxCriteria == 30
    assert S1.minCriteria == 25
    assert S1.propCriteria == [25, 30]
    
    assert S2.maxCriteria == S2.minCriteria
    assert S2.maxCriteria == 50
    assert S2.propCriteria == 50
    