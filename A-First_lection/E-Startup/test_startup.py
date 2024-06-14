from startup import is_profit_of_d
import pytest


@pytest.mark.parametrize('n, k, d, expected_result', [(21, 108, 1, '216'),
                                                      (150, 15, 4, '1500000'),
                                                      (864, 12, 4, '8640000'),
                                                      (34, 18, 5, '3420000')])
def test_has_profit_of_d(n, k, d, expected_result):
    assert is_profit_of_d(n, k, d) == expected_result


@pytest.mark.parametrize('n, k, d, expected_result', [(17, 72, 5, -1),
                                                      (5, 12, 4, -1),
                                                      (3, 74, 1, -1)])
def test_without_profit(n, k, d, expected_result):
    assert is_profit_of_d(n, k, d) == expected_result


@pytest.mark.parametrize('expected_exception, n, k, d', [(ValueError, 'a', 1, 2),
                                                         (TypeError, 1, 'a', 2),
                                                         (TypeError, 1, 2, 'a')])
def test_error(expected_exception, n, k, d):
    with pytest.raises(expected_exception):
        is_profit_of_d(n, k, d)
