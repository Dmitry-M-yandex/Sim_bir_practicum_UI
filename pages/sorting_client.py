from locators.customers import Customer
from pages.base_wrapper import BaseWrapper


class SortingClient(BaseWrapper, Customer):
    def __init__(self, driver):
        super().__init__(driver)

    def list_first_name(self, index):
        soup.select("tr:nth-child > td:nth-child(1)")
        list_name = []
        selector, locator = Customer.COLUMN_FIRST_NAME
        locator = locator.format(index)
        element = self.wait_element((selector, locator))
        return element
