from selenium import webdriver
import data
from pages import UrbanRoutesPage


class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")

        options.set_capability(
            "goog:loggingPrefs",
            {"performance": "ALL"}
        )

        cls.driver = webdriver.Chrome(options=options)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

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

        assert "Supportive" in self.driver.page_source

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

        assert data.CARD_NUMBER[-4:] in self.driver.page_source

    def test_comment_for_driver(self):

        self.driver.get(data.URBAN_ROUTES_URL)

        page = UrbanRoutesPage(self.driver)

        page.set_addresses(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_call_taxi_button()
        page.select_supportive_plan()

        page.add_comment(data.MESSAGE_FOR_DRIVER)

        assert data.MESSAGE_FOR_DRIVER in self.driver.page_source

    def test_order_blanket(self):

        self.driver.get(data.URBAN_ROUTES_URL)

        page = UrbanRoutesPage(self.driver)

        page.set_addresses(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_call_taxi_button()
        page.select_supportive_plan()

        page.order_blanket()

        assert "Blanket" in self.driver.page_source

    def test_order_2_ice_creams(self):

        self.driver.get(data.URBAN_ROUTES_URL)

        page = UrbanRoutesPage(self.driver)

        page.set_addresses(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_call_taxi_button()
        page.select_supportive_plan()

        amount = 2
        page.order_ice_cream(amount)

        assert str(amount) in self.driver.page_source

    def test_car_search_model_appears(self):

        self.driver.get(data.URBAN_ROUTES_URL)

        page = UrbanRoutesPage(self.driver)

        page.set_addresses(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_call_taxi_button()
        page.select_supportive_plan()

        page.enter_phone_number(data.PHONE_NUMBER)
        page.enter_card(data.CARD_NUMBER, data.CARD_CODE)

        page.order_blanket()
        page.click_order()

        assert page.wait_for_car()
