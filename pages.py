from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import helpers


class UrbanRoutesPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ---------- ROUTE ----------

    def set_addresses(self, from_address, to_address):

        from_field = self.wait.until(
            EC.element_to_be_clickable((By.ID, "from"))
        )
        from_field.clear()
        from_field.send_keys(from_address)

        to_field = self.wait.until(
            EC.element_to_be_clickable((By.ID, "to"))
        )
        to_field.clear()
        to_field.send_keys(to_address)

    def click_call_taxi_button(self):

        call_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(),'Call')]")
            )
        )
        call_button.click()

    # ---------- PLAN ----------

    def select_supportive_plan(self):

        supportive_plan = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[contains(@class,'tcard')][.//div[text()='Supportive']]")
            )
        )
        supportive_plan.click()

    # ---------- PHONE ----------

    def enter_phone_number(self, phone):

        phone_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".np-button"))
        )
        phone_button.click()

        phone_input = self.wait.until(
            EC.visibility_of_element_located((By.ID, "phone"))
        )
        phone_input.send_keys(phone)

        next_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Next']"))
        )
        next_button.click()

        code_input = self.wait.until(
            EC.visibility_of_element_located((By.ID, "code"))
        )

        code = helpers.retrieve_phone_code(self.driver)

        code_input.send_keys(code)

        confirm_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Confirm']"))
        )
        confirm_button.click()

    def get_phone_number_value(self):

        phone_text = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".np-text"))
        )

        return phone_text.text

    # ---------- PAYMENT ----------

    def enter_card(self, card_number, card_code):

        payment_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp-button"))
        )
        payment_button.click()

        add_card_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[text()='Add card']"))
        )
        add_card_button.click()

        card_number_input = self.wait.until(
            EC.visibility_of_element_located((By.ID, "number"))
        )
        card_number_input.send_keys(card_number)

        card_code_input = self.wait.until(
            EC.visibility_of_element_located((By.NAME, "code"))
        )
        card_code_input.send_keys(card_code)

        card_code_input.send_keys(Keys.TAB)

        link_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Link']"))
        )
        link_button.click()

    # ---------- COMMENT ----------

    def add_comment(self, message):

        comment_box = self.wait.until(
            EC.visibility_of_element_located((By.ID, "comment"))
        )
        comment_box.send_keys(message)

    # ---------- BLANKET ----------

    def order_blanket(self):

        self.wait.until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, ".overlay"))
        )

        blanket_option = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".r-sw-label"))
        )

        self.driver.execute_script("arguments[0].click();", blanket_option)

    # ---------- ICE CREAM ----------

    def order_ice_cream(self):

        plus_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".counter-plus"))
        )

        plus_button.click()
        plus_button.click()

    # ---------- ORDER TAXI ----------

    def click_order(self):

        self.wait.until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, ".overlay"))
        )

        order_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".smart-button"))
        )

        self.driver.execute_script("arguments[0].click();", order_button)

    # ---------- CAR SEARCH ----------

    def wait_for_car(self):

        car_search = self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".order-header-title")
            )
        )

        return car_search.is_displayed()

    # ---------- ORDER HEADER ----------

    def get_order_header(self):

        return self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "order-header"))
        ).text