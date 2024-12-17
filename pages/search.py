from pages.base_page import BasePage
from pages.locators.locators import SearchLoc as Loc

class Search(BasePage):
    page_url = ''
    def input_search_and_test(self, text):
        input_search = self.find(Loc.input_loc)
        input_search.send_keys(text)
        input_search.submit()
        result_text = self.find(Loc.result_text_loc)
        assert result_text.text == f"Search results for: '{text}'"

