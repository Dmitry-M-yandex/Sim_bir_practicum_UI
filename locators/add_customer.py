from selenium.webdriver.common.by import By


class AddCustomer:
    TAB_ADD_CUSTOMER = (By.XPATH, '//*[@class = "btn btn-lg tab"][@ng-click="addCust()"]')
    FIELD_FIRST_NAME = (By.XPATH, "//*[contains(@class,'form-control ng-pristine')][@placeholder='First Name']")
    FIELD_LAST_NAME = (By.XPATH, "//*[contains(@class,'form-control ng-pristine')][@placeholder='Last Name']")
    FIELD_POST_CODE = (By.XPATH, "//*[contains(@class,'form-control ng-pristine')][@placeholder='Post Code']")
    BUTTON_ADD_CUSTOMER = (By.XPATH, "//*[@class = 'btn btn-default']")