import pytest


@pytest.mark.regression
def test_sale_h1(sale_page):
    sale_page.open_page()
    sale_page.check_text_h1('Sale')