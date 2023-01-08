from selenium.webdriver.common.by import By
import time  # оставил для того чтобы добавить time.sleep() после открытия ссылки для проверки задания


def test_recycle_bin_should_be_present(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    browser.find_element(By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    assert browser.find_elements(By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']"), \
        'basket button not found'

