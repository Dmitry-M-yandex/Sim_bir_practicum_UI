from selenium.webdriver.common.by import By


class Customer:
    TAB_CUSTOMER = (By.XPATH, '//*[@class = "btn btn-lg tab btn-primary"]')
    FIELD_SEARCH_CUSTOMER = (By.XPATH, "//*[contains(@class,'control ng-valid ng-dirty')][@placeholder='Search "
                                       "Customer']")
    COLUMN_FIRST_NAME = (By.XPATH, '//tbody/tr{}/td[1]')
    BUTTON_DELETE = (By.XPATH, '//tr{}/td[5]/button')
