"""
ported from /functional_tests/tests.py
"""
import time

from behave import given, when, then
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys


@given('Edith opens her browser')
def step(context):
    context.browser = Firefox()


@when('Edith goes to the home page')
def step(context):
    context.browser.get(context.test.live_server_url)
    context.browser.set_window_size(1024, 768)


@then('She notices the input box nicely centered')
def step(context):
    inputbox = context.browser.find_element_by_id('id_new_item')
    context.test.assertAlmostEqual(
        inputbox.location['x'] + inputbox.size['width'] / 2,
        512,
        delta=10
    )


@then('She starts a new list and sees the input is nicely centered there, too')
def step(context):
    # She starts a new list and sees the input is nicely centered there too
    inputbox = context.browser.find_element_by_id('id_new_item')
    inputbox.send_keys('testing')
    inputbox.send_keys(Keys.ENTER)
    wait_for_row_in_list_table(context, '1: testing')
    inputbox = context.browser.find_element_by_id('id_new_item')
    context.test.assertAlmostEqual(
        inputbox.location['x'] + inputbox.size['width'] / 2,
        512,
        delta=10
    )


MAX_WAIT = 10


def wait_for_row_in_list_table(context, row_text):
    start_time = time.time()
    while True:
        try:
            table = context.browser.find_element_by_id('id_list_table')
            rows = table.find_elements_by_tag_name('tr')
            context.test.assertIn(row_text, [row.text for row in rows])
            return
        except (AssertionError, WebDriverException) as e:
            if time.time() - start_time > MAX_WAIT:
                raise e
            time.sleep(0.5)
