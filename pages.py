from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import helpers


class UrbanRoutesPage:

    # ---------- LOCATORS ----------

    FROM_FIELD = (By.ID, "from")
    TO_FIELD = (By.ID, "to")

    CALL_BUTTON = (By.XPATH, "//button[contains(text(),'Call')]")

    SUPPORTIVE_PLAN = (
        By.XPATH,
        "//div[contains(@class,'tcard')][.//div[text()='Supportive']]"
    )

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


    COMMENT_BOX = (By.ID, "comment")

    BLANKET_SWITCH = (By.CSS_SELECTOR, ".r-sw-label")


    ICE_CREAM_PLUS = (By.CSS_SELECTOR, ".counter-plus")

    ORDER_BUTTON = (By.CSS_SELECTOR, ".smart-button")

    CAR_SEARCH = (By.CSS_SELECTOR, ".order-header-title")

    OVERLAY = (By.CSS_SELECTOR, ".overlay")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ---------- ROUTE ----------

    def set_addresses(self, from_address, to_address):

        from_field = self.wait.until(
            EC.element_to_be_clickable(self.FROM_FIELD)
        )
        from_field.clear()
        from_field.send_keys(from_address)

        to_field = self.wait.until(
            EC.element_to_be_clickable(self.TO_FIELD)
        )
        to_field.clear()
        to_field.send_keys(to_address)

    def click_call_taxi_button(self):

        call_button = self.wait.until(
            EC.element_to_be_clickable(self.CALL_BUTTON)
        )
        call_button.click()

    # ---------- PLAN ----------

    def select_supportive_plan(self):

        supportive_plan = self.wait.until(
            EC.element_to_be_clickable(self.SUPPORTIVE_PLAN)
        )
        supportive_plan.click()

    # ---------- PHONE ----------

    def enter_phone_number(self, phone):

        phone_button = self.wait.until(
            EC.element_to_be_clickable(self.PHONE_BUTTON)
        )
        phone_button.click()

        phone_input = self.wait.until(
            EC.visibility_of_element_located(self.PHONE_INPUT)
        )
        phone_input.send_keys(phone)

        next_button = self.wait.until(
            EC.element_to_be_clickable(self.NEXT_BUTTON)
        )
        next_button.click()

        code_input = self.wait.until(
            EC.visibility_of_element_located(self.CODE_INPUT)
        )

        code = helpers.retrieve_phone_code(self.driver)

        code_input.send_keys(code)

        confirm_button = self.wait.until(
            EC.element_to_be_clickable(self.CONFIRM_BUTTON)
        )
        confirm_button.click()

    def get_phone_number_value(self):

        phone_text = self.wait.until(
            EC.visibility_of_element_located(self.PHONE_TEXT)
        )

        return phone_text.text

    # ---------- PAYMENT ----------

    def enter_card(self, card_number, card_code):

        payment_button = self.wait.until(
            EC.element_to_be_clickable(self.PAYMENT_BUTTON)
        )
        payment_button.click()

        add_card_button = self.wait.until(
            EC.element_to_be_clickable(self.ADD_CARD_BUTTON)
        )
        add_card_button.click()

        card_number_input = self.wait.until(
            EC.visibility_of_element_located(self.CARD_NUMBER_INPUT)
        )
        card_number_input.send_keys(card_number)

        card_code_input = self.wait.until(
            EC.visibility_of_element_located(self.CARD_CODE_INPUT)
        )
        card_code_input.send_keys(card_code)

        card_code_input.send_keys(Keys.TAB)

        link_button = self.wait.until(
            EC.element_to_be_clickable(self.LINK_BUTTON)
        )
        link_button.click()

        # click X button if present
        try:
            close_button = self.wait.until(
                EC.element_to_be_clickable(self.CLOSE_BUTTON)
            )
            close_button.click()
        except:
            pass

    # ---------- COMMENT ----------

    def add_comment(self, message):

        comment_box = self.wait.until(
            EC.visibility_of_element_located(self.COMMENT_BOX)
        )
        comment_box.send_keys(message)

    # ---------- BLANKET ----------

    def order_blanket(self):
        self.wait.until(
            EC.invisibility_of_element_located(self.OVERLAY)
        )

        blanket = self.wait.until(
            EC.element_to_be_clickable(self.BLANKET_SWITCH)
        )

        self.driver.execute_script("arguments[0].click();", blanket)

    # ---------- ICE CREAM ----------

    def order_ice_cream(self, amount):

        plus_button = self.wait.until(
            EC.element_to_be_clickable(self.ICE_CREAM_PLUS)
        )

        for _ in range(amount):
            plus_button.click()

    # ---------- ORDER TAXI ----------

    def click_order(self):

        self.wait.until(
            EC.invisibility_of_element_located(self.OVERLAY)
        )

        order_button = self.wait.until(
            EC.element_to_be_clickable(self.ORDER_BUTTON)
        )

        self.driver.execute_script("arguments[0].click();", order_button)

    # ---------- CAR SEARCH ----------

    def wait_for_car(self):

        car_search = self.wait.until(
            EC.visibility_of_element_located(self.CAR_SEARCH)
        )

        return car_search.is_displayed()
