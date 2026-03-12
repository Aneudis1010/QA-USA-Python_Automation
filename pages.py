from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import helpers


class UrbanRoutesPage:

    FROM_FIELD = (By.ID, "from")
    TO_FIELD = (By.ID, "to")

    CALL_BUTTON = (By.XPATH, "//button[contains(text(),'Call')]")

    SUPPORTIVE_PLAN = (By.XPATH, "//div[contains(@class,'tcard')][.//div[text()='Supportive']]")
    ACTIVE_PLAN = (By.CSS_SELECTOR, ".tcard.active")

    PHONE_BUTTON = (By.CSS_SELECTOR, ".np-button")
    PHONE_INPUT = (By.ID, "phone")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Next']")
    CODE_INPUT = (By.ID, "code")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Confirm']")
    PHONE_TEXT = (By.CSS_SELECTOR, ".np-text")

    PAYMENT_BUTTON = (By.CSS_SELECTOR, ".pp-button")
    ADD_CARD_BUTTON = (By.XPATH, "//div[text()='Add card']")
    CARD_NUMBER_INPUT = (By.ID, "number")
    CARD_CODE_INPUT = (By.NAME, "code")
    LINK_BUTTON = (By.XPATH, "//button[text()='Link']")
    CLOSE_BUTTON = (By.XPATH, "//button[contains(@class,'close')]")
    ACTIVE_CARD = (By.CSS_SELECTOR, ".pp-value")

    COMMENT_BOX = (By.ID, "comment")

    BLANKET_SWITCH = (By.CSS_SELECTOR, ".r-sw-label")
    BLANKET_CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox']")

    ICE_CREAM_PLUS = (By.CSS_SELECTOR, ".counter-plus")
    ICE_CREAM_COUNTER = (By.CSS_SELECTOR, ".counter-value")

    ORDER_BUTTON = (By.CSS_SELECTOR, ".smart-button")
    CAR_SEARCH = (By.CSS_SELECTOR, ".order-header-title")

    OVERLAY = (By.CSS_SELECTOR, ".overlay")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def set_addresses(self, from_address, to_address):
        self.driver.find_element(*self.FROM_FIELD).send_keys(from_address)
        self.driver.find_element(*self.TO_FIELD).send_keys(to_address)

    def click_call_taxi_button(self):
        self.wait.until(EC.element_to_be_clickable(self.CALL_BUTTON)).click()

    def select_supportive_plan(self):
        self.wait.until(EC.element_to_be_clickable(self.SUPPORTIVE_PLAN)).click()

    def enter_phone_number(self, phone):

        self.wait.until(EC.element_to_be_clickable(self.PHONE_BUTTON)).click()
        self.wait.until(EC.visibility_of_element_located(self.PHONE_INPUT)).send_keys(phone)

        self.wait.until(EC.element_to_be_clickable(self.NEXT_BUTTON)).click()

        code_input = self.wait.until(EC.visibility_of_element_located(self.CODE_INPUT))
        code = helpers.retrieve_phone_code(self.driver)

        code_input.send_keys(code)

        self.wait.until(EC.element_to_be_clickable(self.CONFIRM_BUTTON)).click()

    def enter_card(self, card_number, card_code):

        self.wait.until(EC.element_to_be_clickable(self.PAYMENT_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(self.ADD_CARD_BUTTON)).click()

        self.wait.until(
            EC.visibility_of_element_located(self.CARD_NUMBER_INPUT)
        ).send_keys(card_number)

        code_input = self.wait.until(
            EC.visibility_of_element_located(self.CARD_CODE_INPUT)
        )

        code_input.send_keys(card_code)
        code_input.send_keys(Keys.TAB)

        self.wait.until(EC.element_to_be_clickable(self.LINK_BUTTON)).click()

        close_buttons = self.driver.find_elements(*self.CLOSE_BUTTON)
        if close_buttons:
            self.driver.execute_script("arguments[0].click();", close_buttons[0])

    def add_comment(self, message):
        self.wait.until(EC.visibility_of_element_located(self.COMMENT_BOX)).send_keys(message)

    def order_blanket(self):

        blanket = self.wait.until(
            EC.element_to_be_clickable(self.BLANKET_SWITCH)
        )

        self.driver.execute_script("arguments[0].click();", blanket)

    def order_ice_cream(self, amount):

        plus = self.wait.until(EC.element_to_be_clickable(self.ICE_CREAM_PLUS))

        for _ in range(amount):
            plus.click()

    def click_order(self):

        self.wait.until(
            EC.invisibility_of_element_located(self.OVERLAY)
        )

        order_button = self.wait.until(
            EC.element_to_be_clickable(self.ORDER_BUTTON)
        )

        self.driver.execute_script(
            "arguments[0].click();", order_button
        )

    # ---------- GETTERS ----------

    def get_from(self):
        return self.driver.find_element(*self.FROM_FIELD).get_property("value")

    def get_to(self):
        return self.driver.find_element(*self.TO_FIELD).get_property("value")

    def get_active_plan(self):
        return self.driver.find_element(*self.ACTIVE_PLAN).text

    def get_phone_number_value(self):
        return self.driver.find_element(*self.PHONE_TEXT).text

    def get_active_card(self):
        return self.driver.find_element(*self.ACTIVE_CARD).text

    def get_comment(self):
        return self.driver.find_element(*self.COMMENT_BOX).get_property("value")

    # ✔ Correct slider state validation
    def get_blanket_state(self):
        self.wait.until(
            EC.presence_of_element_located(self.BLANKET_CHECKBOX)
        )
        return self.driver.find_element(*self.BLANKET_CHECKBOX).is_selected()

    def get_ice_cream_count(self):
        return self.driver.find_element(*self.ICE_CREAM_COUNTER).text

    def get_car_search_modal(self):
        return self.driver.find_element(*self.CAR_SEARCH).is_displayed()
