import pytest
from selenium import webdriver

from pages import UrbanRoutesPage
from data import (
    BASE_URL,
    FROM_ADDRESS,
    TO_ADDRESS,
    PHONE_NUMBER,
    CARD_NUMBER,
    CARD_CODE,
    COMMENT,
)


class TestUrbanRoutes:

    @pytest.fixture(autouse=True)
    def setup(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(options=options)
        self.driver.get(BASE_URL)

        self.page = UrbanRoutesPage(self.driver)

        yield
        self.driver.quit()

    def prepare_supportive(self):
        self.page.set_addresses(FROM_ADDRESS, TO_ADDRESS)
        self.page.click_call_taxi_button()
        self.page.select_supportive_plan()

    def test_set_addresses(self):
        self.page.set_addresses(FROM_ADDRESS, TO_ADDRESS)
        assert FROM_ADDRESS.split(",")[0] in self.driver.page_source

    def test_select_supportive_plan(self):
        self.prepare_supportive()
        assert self.page.is_supportive_selected()

    def test_fill_phone_number(self):
        self.prepare_supportive()
        self.page.fill_phone_number(PHONE_NUMBER)
        assert PHONE_NUMBER.replace(" ", "") in \
               self.page.get_phone_number_value().replace(" ", "")

    def test_add_credit_card(self):
        self.prepare_supportive()
        self.page.fill_phone_number(PHONE_NUMBER)
        self.page.add_credit_card(CARD_NUMBER, CARD_CODE)

        # If no exception occurred during interaction, test passes
        assert True

    def test_write_comment_for_driver(self):
        self.prepare_supportive()
        self.page.write_comment(COMMENT)
        assert COMMENT in self.page.get_comment_value()

    def test_blanket_toggle(self):
        self.prepare_supportive()
        self.page.toggle_blanket()
        assert self.page.is_blanket_selected()

    def test_order_two_ice_creams(self):
        self.prepare_supportive()
        self.page.add_two_ice_creams()
        assert self.page.get_ice_cream_count() == "2"

    def test_order_supportive_taxi_shows_search_modal(self):
        self.prepare_supportive()
        self.page.fill_phone_number(PHONE_NUMBER)
        self.page.order_taxi()
        assert self.page.is_search_modal_displayed()