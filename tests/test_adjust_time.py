from adjust_time.adjust_time import adjust_date

def test_plus_time():
    assert adjust_date('2018-10-01', 1) == '2018-10-02'

def test_minus_time():
    assert adjust_date('2018-10-01', -1) == '2018-09-30'