import pytest
from selenium import webdriver
import data
from pages import UrbanRoutesPage


class TestUrbanRoutes:

    @pytest.fixture(autouse=True)
    def setup(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")

        options.set_capability(
            "goog:loggingPrefs",
            {"performance": "ALL"}
        )

        self.driver = webdriver.Chrome(options=options)

        yield

        self.driver.quit()

    def test_set_route(self):

        self.driver.get(data.URBAN_ROUTES_URL)

        page = UrbanRoutesPage(self.driver)

        page.set_addresses(data.ADDRESS_FROM, data.ADDRESS_TO)

        assert data.ADDRESS_FROM.split(",")[0] in self.driver.page_source

    def test_select_supportive_plan(self):

        self.driver.get(data.URBAN_ROUTES_URL)

        page = UrbanRoutesPage(self.driver)

        page.set_addresses(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_call_taxi_button()
        page.select_supportive_plan()

    def test_fill_phone_number(self):

        self.driver.get(data.URBAN_ROUTES_URL)

        page = UrbanRoutesPage(self.driver)

        page.set_addresses(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_call_taxi_button()
        page.select_supportive_plan()

        page.enter_phone_number(data.PHONE_NUMBER)

        assert page.get_phone_number_value() == data.PHONE_NUMBER

    def test_fill_card(self):

        self.driver.get(data.URBAN_ROUTES_URL)

        page = UrbanRoutesPage(self.driver)

        page.set_addresses(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_call_taxi_button()
        page.select_supportive_plan()

        page.enter_phone_number(data.PHONE_NUMBER)
        page.enter_card(data.CARD_NUMBER, data.CARD_CODE)

    def test_comment_for_driver(self):

        self.driver.get(data.URBAN_ROUTES_URL)

        page = UrbanRoutesPage(self.driver)

        page.set_addresses(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_call_taxi_button()
        page.select_supportive_plan()

        page.add_comment(data.MESSAGE_FOR_DRIVER)

    def test_order_blanket(self):

        self.driver.get(data.URBAN_ROUTES_URL)

        page = UrbanRoutesPage(self.driver)

        page.set_addresses(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_call_taxi_button()
        page.select_supportive_plan()

        page.order_blanket()

    def test_order_2_ice_creams(self):

        self.driver.get(data.URBAN_ROUTES_URL)

        page = UrbanRoutesPage(self.driver)

        page.set_addresses(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_call_taxi_button()
        page.select_supportive_plan()

        page.order_ice_cream()

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)

        page = UrbanRoutesPage(self.driver)

        page.set_addresses(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_call_taxi_button()
        page.select_supportive_plan()

        page.enter_phone_number(data.PHONE_NUMBER)
        page.enter_card(data.CARD_NUMBER, data.CARD_CODE)

        page.order_blanket()

        page.click_order()  # correct action
        assert page.wait_for_car()  # verify search modal