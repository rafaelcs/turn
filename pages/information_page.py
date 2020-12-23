from locators.information_page_locators import InformationPageLocators
from pages.base_page import BasePage

class InformationPage(BasePage):

    def fill_in_personal_details(
        self,
        first_name: str,
        last_name: str,
        middle_name: str,
        dob_month: str,
        dob_day: str,
        dob_year: str,
        gender: str,
        ssn: str,
    ):
        self.send_keys(InformationPageLocators.FIRST_NAME_TEXT_FIELD, first_name)
        self.send_keys(InformationPageLocators.LAST_NAME_TEXT_FIELD, last_name)
        self.send_keys(InformationPageLocators.MIDDLE_NAME_TEXT_FIELD, middle_name)
        self.select_value_from_dropdown(InformationPageLocators.DOB_MONTH_DROPDOWN, dob_month)
        self.select_value_from_dropdown(InformationPageLocators.DOB_DAY_DROPDOWN, dob_day.strip('0'))
        self.select_value_from_dropdown(InformationPageLocators.DOB_YEAR_DROPDOWN, dob_year)
        self.select_value_from_dropdown(InformationPageLocators.GENDER_DROPDOWN, gender)
        self.click(InformationPageLocators.SSN_TEXT_FIELD)
        self.send_keys(InformationPageLocators.SSN_TEXT_FIELD, ssn)

    def fill_in_contact_details(
        self,
        zip_code: str,
        email: str,
        phone_number: str,
        driver_license_state: str,
        driver_license_number: str,
    ):
        self.click(InformationPageLocators.ZIPCODE_TEXT_FIELD)
        self.send_keys(InformationPageLocators.ZIPCODE_TEXT_FIELD, zip_code)
        self.send_keys(InformationPageLocators.EMAIL_TEXT_FIELD, email)
        self.send_keys(InformationPageLocators.PHONE_TEXT_FIELD, phone_number)
        self.select_value_from_dropdown(InformationPageLocators.DRIVER_LICENSE_DROPDOWN, driver_license_state)
        self.click(InformationPageLocators.DRIVER_LICENSE_NUMBER_TEXT_FIELD)
        self.send_keys(InformationPageLocators.DRIVER_LICENSE_NUMBER_TEXT_FIELD, driver_license_number)

    def accept_terms_and_conditions(self, accept_terms: bool):
        if accept_terms:
            self.click(InformationPageLocators.TERMS_AND_CONDITIONS_CHECKBOX)
