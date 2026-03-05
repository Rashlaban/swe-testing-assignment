from quick_calc.app import QuickCalc


def test_full_flow_addition_5_plus_3_equals_8():
    calc = QuickCalc()
    calc.press("5")
    calc.press("+")
    calc.press("3")
    result = calc.press("=")
    assert result == "8"


def test_clear_resets_after_calculation():
    calc = QuickCalc()
    calc.press("9")
    calc.press("*")
    calc.press("9")
    calc.press("=")
    assert calc.display == "81"
    assert calc.press("C") == "0"