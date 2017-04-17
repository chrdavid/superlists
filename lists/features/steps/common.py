from behave import given, when, then


@given('server is running')
def step_impl(context):
    pass


@when('requesting \'{url}\'')
def step_impl(context, url):
    context.response = context.test.client.get(url)


@then('server renders \'{template}\' template')
def step_impl(context, template):
    context.test.assertTemplateUsed(context.response, template)
