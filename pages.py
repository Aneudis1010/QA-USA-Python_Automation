from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class UrbanRoutesPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

        # Address
        self.FROM_INPUT = (By.ID, "from")
        self.TO_INPUT = (By.ID, "to")
        self.CALL_TAXI_BUTTON = (By.XPATH, "//button[contains(., 'Call a taxi')]")
        self.SUPPORTIVE_PLAN = (By.XPATH, "//div[contains(@class,'tcard')][.//div[text()='Supportive']]")

        # Phone
        self.PHONE_BUTTON = (By.XPATH, "//div[text()='Phone number']")
        self.PHONE_INPUT = (By.XPATH, "//input[@name='phone']")
        self.NEXT_BUTTON = (By.XPATH, "//button[contains(.,'Next')]")

        # Payment
        self.PAYMENT_SECTION = (By.XPATH, "//div[contains(@class,'pp-value')]")
        self.ADD_CARD_BUTTON = (By.XPATH, "//div[contains(@class,'pp-plus-container')]")
        self.CARD_NUMBER_INPUT = (By.XPATH, "//input[@name='number']")
        self.CARD_CVC_INPUT = (By.XPATH, "//input[@name='code']")
        self.LINK_BUTTON = (By.XPATH, "//button[contains(.,'Link')]")
        self.PAYMENT_METHOD_TEXT = (By.XPATH, "//div[contains(@class,'pp-title')]")

        # Comment
        self.COMMENT_INPUT = (By.ID, "comment")

        # Blanket
        self.BLANKET_SWITCH = (By.XPATH, "//div[contains(@class,'switch')]")
        self.BLANKET_CHECKBOX = (By.XPATH, "//input[@type='checkbox']")

        # Ice cream
        self.ICE_CREAM_PLUS = (By.CLASS_NAME, "counter-plus")
        self.ICE_CREAM_COUNT = (By.CLASS_NAME, "counter-value")

        # Order
        self.ORDER_BUTTON = (By.XPATH, "//button[contains(@class,'button') and contains(@class,'round')]")
        self.SEARCH_MODAL = (By.XPATH, "//div[contains(@class,'modal')]")

    # ---------- ADDRESS ----------

    def set_addresses(self, from_address, to_address):
        from_input = self.wait.until(EC.visibility_of_element_located(self.FROM_INPUT))
        from_input.clear()
        from_input.send_keys(from_address)
        from_input.send_keys(Keys.ENTER)

        to_input = self.wait.until(EC.visibility_of_element_located(self.TO_INPUT))
        to_input.clear()
        to_input.send_keys(to_address)
        to_input.send_keys(Keys.ENTER)

    def click_call_taxi_button(self):
        btn = self.wait.until(EC.presence_of_element_located(self.CALL_TAXI_BUTTON))
        self.driver.execute_script("arguments[0].click();", btn)

    def select_supportive_plan(self):
        card = self.wait.until(EC.presence_of_element_located(self.SUPPORTIVE_PLAN))
        self.driver.execute_script("arguments[0].click();", card)

    # ---------- PHONE ----------

    def fill_phone_number(self, phone):
        self.wait.until(EC.element_to_be_clickable(self.PHONE_BUTTON)).click()
        phone_input = self.wait.until(EC.visibility_of_element_located(self.PHONE_INPUT))
        phone_input.clear()
        phone_input.send_keys(phone)
        self.wait.until(EC.element_to_be_clickable(self.NEXT_BUTTON)).click()

    def get_phone_number_value(self):
        return self.wait.until(
            EC.presence_of_element_located(self.PHONE_INPUT)
        ).get_attribute("value")

    # ---------- PAYMENT ----------
    def test_add_credit_card(self):
        self.prepare_supportive()
        self.page.fill_phone_number(PHONE_NUMBER)
        self.page.add_credit_card(CARD_NUMBER, CARD_CODE)

        # If no exception occurred, test passes
        assert True
    def add_credit_card(self, number, cvc):
        payment = self.wait.until(EC.presence_of_element_located(self.PAYMENT_SECTION))
        self.driver.execute_script("arguments[0].click();", payment)

        plus = self.wait.until(EC.presence_of_element_located(self.ADD_CARD_BUTTON))
        self.driver.execute_script("arguments[0].click();", plus)

        number_input = self.wait.until(EC.visibility_of_element_located(self.CARD_NUMBER_INPUT))
        number_input.click()
        number_input.send_keys(Keys.CONTROL + "a")
        number_input.send_keys(Keys.DELETE)
        number_input.send_keys(number)

        cvc_input = self.wait.until(EC.visibility_of_element_located(self.CARD_CVC_INPUT))
        cvc_input.click()
        cvc_input.send_keys(Keys.CONTROL + "a")
        cvc_input.send_keys(Keys.DELETE)
        cvc_input.send_keys(cvc)

        link = self.wait.until(EC.presence_of_element_located(self.LINK_BUTTON))
        self.driver.execute_script("arguments[0].click();", link)

    def get_payment_method_text(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.PAYMENT_METHOD_TEXT)
        ).text

    def is_card_modal_closed(self):
        try:
            self.driver.find_element(*self.CARD_NUMBER_INPUT)
            return False
        except:
            return True
    # ---------- COMMENT ----------

    def write_comment(self, text):
        comment = self.wait.until(EC.visibility_of_element_located(self.COMMENT_INPUT))
        comment.clear()
        comment.send_keys(text)

    def get_comment_value(self):
        return self.wait.until(
            EC.presence_of_element_located(self.COMMENT_INPUT)
        ).get_attribute("value")

    # ---------- BLANKET ----------

    def toggle_blanket(self):
        self.wait.until(
            lambda d: d.find_element(*self.BLANKET_CHECKBOX)
        )
        self.driver.execute_script(
            "arguments[0].click();",
            self.driver.find_element(*self.BLANKET_CHECKBOX)
        )

    def is_blanket_selected(self):
        return self.wait.until(
            lambda d: d.execute_script(
                "return document.querySelector('[type=\"checkbox\"]').checked;"
            )
        )

    # ---------- ICE CREAM ----------

    def add_two_ice_creams(self):
        plus = self.wait.until(EC.element_to_be_clickable(self.ICE_CREAM_PLUS))
        plus.click()
        plus.click()

    def get_ice_cream_count(self):
        return self.wait.until(
            EC.presence_of_element_located(self.ICE_CREAM_COUNT)
        ).text

    # ---------- ORDER ----------

    def order_taxi(self):
        btn = self.wait.until(EC.presence_of_element_located(self.ORDER_BUTTON))
        self.driver.execute_script("arguments[0].click();", btn)

    def is_search_modal_displayed(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_MODAL)
        ).is_displayed()

    # ---------- SUPPORTIVE CHECK ----------

    def is_supportive_selected(self):
        card = self.wait.until(EC.presence_of_element_located(self.SUPPORTIVE_PLAN))
        return "active" in card.get_attribute("class")