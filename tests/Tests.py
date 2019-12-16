from time import sleep
from tests.Pages import SearchHelper
from tests.tempmail import *
from bs4 import BeautifulSoup

# Date                 : 12.12.2019
# Author               : Gevorg Iritsyan <gevorg.iritsyan@gmail.com>
# Description          : Autotest with pytest_report and ALLURE plugins for generating HTML reports

# How_to_run with pytest_report : $ pytest --html=report.html Tests.py
# How to generate allure report : $ allure generate directory-with-results/ -o directory-where-u-want-indexhtmlreport-
#                                   -to-be-generated/
# How_to_run with ALLURE        : $ pytest /path_to_directory_to/Tests.py --alluredir=/path_to_directory_to/allure_data
# How to see allure report      : $ ./allure open 'path_to_directory_allure_reports/allure_reports/'

#  pytest /Users/gevfolder/PycharmProjects/autotests/tests/Tests.py --alluredir=/Users/gevfolder/PycharmProjects/autotests/tests/allure_data
# ./allure open '/Users/gevfolder/PycharmProjects/autotests/tests/allure_reports/'


def test_download_and_signing_up(chrome_driver):
    main_page = SearchHelper(chrome_driver)
    main_page.click_on_menu_button()
    main_page.menu_click_on_cleanmymac_x()
    main_page.cleanmymac_x_click_dawnload()
    x = get_email_address()
    main_page.cleanmymac_x_pop_up_enter_mail(x)
    main_page.cleanmymac_x_pop_up_subscribe()

    h = get_email_hash(x)
    sleep(10)
    email = get_emails(h)
    soup = BeautifulSoup(email[0]['mail_text_only'])
    page_link = soup.find_all('a', class_='btn')[0].attrs['href']
    main_page.confirm_subscription(page_link)
    check_mail(x)
    assert_actual_vs_expected(test_download_and_signing_up,
                              main_page.lets_get_social_were_always_on(),
                              'Let’s get social. We’re always on.')


def assert_actual_vs_expected(test_name, expected, actual):
    assert actual == expected, f"{test_name}EXPECTED>>{expected}<<DIFFERS FROM ACTUAL>>{actual}<<:"


