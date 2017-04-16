"""
Some basic tests to understand Scenario outlines
"""
from behave import then, given, when


def blend(x):
    return {
        'thing': 'other thing',
        'Red Tree Frog': 'mush',
        'iPhone': 'toxic waste',
        'Galaxy Nexus': 'toxic waste'
    }[x]


@when(u'I switch the blender on')
def step_impl(context):
    context.blender = True


@given(u'I put {value} in a blender,')
def step_impl(context, value):
    context.input = value


@then(u'it should transform into {value}')
def step_impl(context, value):
    context.test.assertEqual(value, blend(context.input))
