import pytest
@pytest.mark.regression
def test_search_pants(search):
    search.open_page()
    search.input_search_and_test('kek')
