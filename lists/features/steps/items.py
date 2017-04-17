from behave import when, then

from lists.models import List, Item


@then('item count is {count:d}')
def step_impl(context, count):
    context.test.assertEqual(Item.objects.count(), count)


@when('creating an item with text "{text}"')
def step_impl(context, text):
    list_ = List.objects.create()
    Item.objects.create(text=text, list=list_)


@when(u'sending a POST request to \'{url}\' with item_text \'{text}\'')
def step_impl(context, url, text):
    if url == '/lists/%d/add_item':
        context.response = context.test.client.post(url % context.list.id, data={'item_text': text})
    else:
        context.response = context.test.client.post(url, data={'item_text': text})


@when('adding an item with text "{text}" to {a_list}')
def step_impl(context, text, a_list):
    if a_list == 'the list':
        Item.objects.create(text=text, list=context.list)
    else:
        Item.objects.create(text=text, list=context.other_list)


@then('there are {count:d} item(s) in the database')
def step_impl(context, count):
    context.test.assertEqual(Item.objects.count(), count)


@then('the item at position {position:d} has the text "{text}"')
def step_impl(context, position, text):
    context.test.assertEqual(text, Item.objects.all()[position].text)


@then(u'the item\'s text is \'{text}\'')
def step_impl(context, text):
    item = Item.objects.first()
    context.test.assertEqual(text, item.text)


@then(u'the item\'s list is our earlier created list')
def step_impl(context):
    item = Item.objects.first()
    context.test.assertEqual(item.list, context.list)
