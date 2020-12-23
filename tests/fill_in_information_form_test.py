import pytest
import allure

from pages.information_page import InformationPage
from pages.base_page import BasePage
from faker import Faker


@pytest.mark.usefixtures('driver')
@allure.feature('Fill in the information form')
class TestFillInInformationForm:

    def setup_class(self):
        self.information_page = InformationPage(self.driver)
        self.base_page = BasePage(self.driver)
        self.fake = Faker()

        # visit the page
        self.base_page.visit()

    @allure.title('should fill in the personal details')
    def test_fill_in_personal_details_form(self):
        self.information_page.fill_in_personal_details(
            first_name=self.fake.first_name(),
            last_name=self.fake.last_name(),
            middle_name=self.fake.last_name(),
            dob_month=self.fake.month_name(),
            dob_day=self.fake.day_of_month(),
            dob_year=self.fake.year(),
            gender='male',
            ssn=self.fake.ssn()
        )

    @allure.title('should fill in the contact details')
    def test_fill_in_contact_details_form(self):
        self.information_page.fill_in_contact_details(
            zip_code=self.fake.zipcode(),
            email=self.fake.company_email(),
            phone_number=self.fake.phone_number(),
            driver_license_state=self.fake.state(),
            driver_license_number=self.fake.building_number()
        )

    @allure.title('should accept terms and conditions')
    def test_accept_terms(self):
        self.information_page.accept_terms_and_conditions(accept_terms=True)
