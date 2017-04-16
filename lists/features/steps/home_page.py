from behave import when, then

from lists.models import Item


@when('Requesting \'{url}\'')
def step_impl(context, url):
    context.response = context.test.client.get(url)


@then('Server renders \'{template}\' template.')
def step_impl(context, template):
    context.test.assertTemplateUsed(context.response, template)


@then('Item count is {count:d}.')
def step_impl(context, count):
    context.test.assertEqual(Item.objects.count(), count)
