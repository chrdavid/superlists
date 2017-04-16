"""
ported from /functional_tests/tests.py
"""

from behave import given, when, then
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys

from features.utils import wait_for_row_in_list_table


@given('Edith has opened her browser')
def step(context):
    context.browser = Firefox()


@when('Edith goes to the home page')
def step(context):
    context.browser.get(context.test.live_server_url)


@then('She notices the input box nicely centered')
def step(context):
    context.browser.set_window_size(1024, 768)
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


@then('She notices the page title and header mention to-do lists')
def step_impl(context):
    context.test.assertIn('To-Do', context.browser.title)
    header = context.browser.find_element_by_tag_name("h1").text
    context.test.assertIn('To-Do', header)


@then('She is invited to enter a to-do item straight away')
def step_impl(context):
    inputbox = context.browser.find_element_by_id('id_new_item')
    context.test.assertEqual(
        inputbox.get_attribute('placeholder'),
        'Enter a to-do item'
    )


@then('She types "{text}" into the text box and hit\'s enter')
def step_impl(context, text):
    inputbox = context.browser.find_element_by_id('id_new_item')
    inputbox.send_keys(text)
    inputbox.send_keys(Keys.ENTER)


@then('The page now lists "{idx}: {text}" as an item')
def step_ipl(context, idx, text):
    wait_for_row_in_list_table(context, '%d: %s' % (int(idx), text))


@then(u'There is still a text box inviting her to add another item.')
def step_impl(context):
    context.browser.find_element_by_id('id_new_item')
