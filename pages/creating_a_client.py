from helpers.generate_random_client import GenerateRandomClient
from locators.add_customer import AddCustomer
from pages.base_wrapper import BaseWrapper


class CreatingClient(BaseWrapper, AddCustomer, GenerateRandomClient):
    def __init__(self, driver):
        super().__init__(driver)

    def click_tab_add_customer(self):
        self.find_element(self.TAB_ADD_CUSTOMER).click()

    def fill_first_name(self):
        first_name = self.post_code_to_first_name()
        self.clear_and_send_keys(self.FIELD_FIRST_NAME, first_name)
        return first_name

    def fill_last_name(self):
        last_name = self.generate_last_name()
        self.clear_and_send_keys(self.FIELD_LAST_NAME, last_name)

    def fill_post_code(self):
        post_code = self.generate_post_code()
        self.clear_and_send_keys(self.FIELD_POST_CODE, post_code)

    def click_button_add_customer(self):
        self.find_element(self.BUTTON_ADD_CUSTOMER).click()
