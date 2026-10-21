from research.analysis import make_demo_data, simple_ols_coefficients

def test_demo_data_is_reproducible():
    assert make_demo_data().equals(make_demo_data())

def test_coefficients_are_finite_and_reasonable():
    intercept, effect = simple_ols_coefficients(make_demo_data())
    assert abs(intercept) < 10
    assert abs(effect) < 10
