from selenium.webdriver.common.by import By

class InformationPageLocators:
    FIRST_NAME_TEXT_FIELD = (By.ID, 'firstName')
    LAST_NAME_TEXT_FIELD = (By.ID, 'lastName')
    MIDDLE_NAME_TEXT_FIELD = (By.ID, 'middleName')
    DOB_MONTH_DROPDOWN = (By.XPATH, '//*[@role="button"][1]')
    DOB_DAY_DROPDOWN = (By.XPATH, '//div[4]/div/div[2]/div/div')
    DOB_YEAR_DROPDOWN = (By.XPATH, '//div[4]/div/div[3]/div/div')
    GENDER_DROPDOWN = (By.XPATH, '//div[5]/div/div/div')
    SSN_TEXT_FIELD = (By.XPATH, '//*[@id="ssn"]')
    ZIPCODE_TEXT_FIELD = (By.ID, 'zipcode')
    EMAIL_TEXT_FIELD = (By.ID, 'email')
    PHONE_TEXT_FIELD = (By.ID, 'phone')
    DRIVER_LICENSE_DROPDOWN = (By.XPATH, '//div[10]/div/div/div')
    DRIVER_LICENSE_NUMBER_TEXT_FIELD = (By.ID, 'driversLicenseNumber')
    OPTIONS_FROM_DROPDOWN = (By.XPATH, '//*[@role="option"]')
    TERMS_AND_CONDITIONS_CHECKBOX = (By.XPATH, '//div[2]/label/span')
    FORM = (By.TAG_NAME, 'form')