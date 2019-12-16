import pytest
from selenium import webdriver

# Fixture for Chrome
@pytest.fixture(scope="session")
def chrome_driver():
    driver = webdriver.Chrome(executable_path="../drivers/chromedriver")
    driver.maximize_window()
    yield driver
    driver.quit()


# Fixture for Firefox
@pytest.fixture(scope="session")
def ff_driver():
    ff_driver = webdriver.Firefox()
    yield ff_driver
    ff_driver.quit()
