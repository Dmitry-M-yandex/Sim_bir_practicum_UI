import time
from idlelib import browser
from telnetlib import EC
import wait
from pages.creating_a_client import CreatingClient


def test_creating_client(driver):
    cl_page = CreatingClient(driver)
    cl_page.click_tab_add_customer()
    cl_page.fill_first_name()
    cl_page.fill_last_name()
    cl_page.fill_post_code()
    cl_page.click_button_add_customer()
    try:
        wait.until(EC.alert_is_present())
        driver.switch_to.alert.accept()
        print("Alert accepted")
    except:
        print("no Alert found")
