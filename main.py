from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
import data
import helpers
from pages import UrbanRoutesPage


class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        # Do not modify this method
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check that the server is on and still running.")

    def test_set_route(self):

        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)

        page.set_addresses(data.ADDRESS_FROM, data.ADDRESS_TO)

        assert page.get_from() == data.ADDRESS_FROM
        assert page.get_to() == data.ADDRESS_TO

    def test_select_supportive_plan(self):

        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)

        page.set_addresses(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_call_taxi_button()
        page.select_supportive_plan()

        assert "Supportive" in page.get_active_plan()

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

        assert data.CARD_NUMBER[-4:] in page.get_active_card()

    def test_comment_for_driver(self):

        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)

        page.set_addresses(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_call_taxi_button()
        page.select_supportive_plan()

        page.add_comment(data.MESSAGE_FOR_DRIVER)

        assert page.get_comment() == data.MESSAGE_FOR_DRIVER

    def test_order_blanket(self):

        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)

        page.set_addresses(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_call_taxi_button()
        page.select_supportive_plan()

        page.order_blanket()

        assert page.get_blanket_state()

    def test_order_2_ice_creams(self):

        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)

        page.set_addresses(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_call_taxi_button()
        page.select_supportive_plan()

        amount = 2
        page.order_ice_cream(amount)

        assert page.get_ice_cream_count() == str(amount)

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

        assert page.get_car_search_modal()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
