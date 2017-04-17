from behave import when, then
from selenium.webdriver.common.keys import Keys

from features.utils import wait_for_row_in_list_table


@when('Edith starts a new todo list')
def step_impl(context):
    context.browser.get(context.test.live_server_url)
    inputbox = context.browser.find_element_by_id('id_new_item')
    inputbox.send_keys('Buy peacock feathers')
    inputbox.send_keys(Keys.ENTER)
    wait_for_row_in_list_table(context, '1: Buy peacock feathers')


@then('She notices that her list has a unique URL')
def step_impl(context):
    context.edith_list_url = context.browser.current_url
    context.test.assertRegex(context.edith_list_url, '/lists/.+')


@when('Francis visits the home page, there is no sign of Edith\'s list')
def step_impl(context):
    context.browser.get(context.test.live_server_url)
    page_text = context.browser.find_element_by_tag_name('body').text
    context.test.assertNotIn('Buy peacock feathers', page_text)


@then('Francis starts a new list by entering a new item.')
def step_impl(context):
    inputbox = context.browser.find_element_by_id('id_new_item')
    inputbox.send_keys('Buy milk')
    inputbox.send_keys(Keys.ENTER)
    wait_for_row_in_list_table(context, '1: Buy milk')


@then('Francis gehts his own unique URL')
def step_impl(context):
    context.francis_list_url = context.browser.current_url
    context.test.assertRegex(context.francis_list_url, '/lists/.+')
    context.test.assertNotEqual(context.francis_list_url, context.edith_list_url)


@then('again, there is no trace of Edith\'s list')
def step_impl(context):
    page_text = context.browser.find_element_by_tag_name('body').text
    context.test.assertNotIn('Buy peacock feathers', page_text)
    context.test.assertIn('Buy milk', page_text)
