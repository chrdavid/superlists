from behave import then, when

from lists.models import List, Item


@when('creating a list')
def step_impl(context):
    context.list = List.objects.create()


@when('opening the view for {a_list}')
def step_impl(context, a_list):
    if a_list == 'the list':
        context.response = context.test.client.get('/lists/%d/' % context.list.id)
    else:
        context.response = context.test.client.get('/lists/%d/' % context.other_list.id)


@when('creating another list')
def step_impl(context):
    context.other_list = List.objects.create()


@when(u'send a GET request to \'{url}\'')
def step_impl(context, url):
    context.response = context.test.client.get(url)


@then('the response contains "{text}"')
def step_impl(context, text):
    context.test.assertContains(context.response, text)


@then('the response does not contain "{text}"')
def step_impl(context, text):
    context.test.assertNotContains(context.response, text)


@then('the response context references this list')
def step_impl(context):
    context.test.assertEqual(context.response.context['list'], context.list)


@then(u'the server redirects to the list\'s view')
def step_impl(context):
    if hasattr(context, 'list'):
        list_ = context.list
    else:
        list_ = List.objects.first()
    context.test.assertRedirects(context.response, '/lists/%d/' % list_.id)


@then(u'the server redirects to \'{url}\' without saving an item')
def step_impl(context, url):
    context.test.assertEqual(Item.objects.count(), 0)
    context.test.assertRedirects(context.response, url)
