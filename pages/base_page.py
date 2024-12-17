from selenium.webdriver.remote.webdriver import WebDriver # это чтобы pycharm давал подсказки при вводе driver (вписываем его в инициализацию класса)

class BasePage():

    base_url = 'https://magento.softwaretestingboard.com' # cоздаем чтобы можно было перетащить в BasePage
    page_url = None    # метод open_page так как мы юзаем его на каждой странице, просто пишем разные ссылки

    def __init__(self, driver: WebDriver): # передаем драйвер при инициализации класса (:WebDriver - это чтобы pycharm давал подсказки при вводе driver)
        self.driver = driver

    def open_page(self):
        self.driver.get(f'{self.base_url}{self.page_url}') # собираем ссылку из переданных элементов, где page_url указывается для каждой страницы отдельно

    def find(self, locator: tuple): # что бы не писать каждый раз self.driver.find_element() юзаем это
        return self.driver.find_element(*locator) # *locator - позволяет распаковать переданный в метод картеж
                                           # из (By.ID, 'send2'), сделать это By.ID, 'send2'
        # чтобы НЕ получилось вот так self.driver.find_element((By.ID, 'send2'))

    def find_all(self, locator: tuple): # для того чтобы находить однотипные элементы на странице
        return  self.driver.find_elements(*locator) # например все товары на старнице (автоматом создаст список из них)

