from tax_calculator import calculate_telecom_tax

def test_calculate_telecom_tax():
    """100 birimlik tutar için %18 vergi hesaplamasını doğrular."""
    assert calculate_telecom_tax(100.0) == 18.0