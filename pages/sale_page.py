from pages.locators.locators import SalePageLoc as Loc
from pages.base_page import BasePage



class Sale(BasePage):
    page_url = '/sale.html'

    def check_text_h1(self, text):
        sale_text = self.find(Loc.sale_text_loc)
        assert sale_text.text == text