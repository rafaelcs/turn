import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope='session')
def driver(request):
    custom_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=custom_options)
    driver.maximize_window()

    for item in request.node.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, 'driver', driver)
    yield driver
    driver.quit()