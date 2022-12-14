from behave import step
from nose.tools import assert_equal, assert_is_not_none
import requests
import wget


@step('I send a GET request to Coffee image')
def send_get_fact(context):
    context.response = requests.get('https://coffee.alexflipnote.dev/random')


@step('I send a GET request to Coffee JSON')
def send_get_fact(context):
    context.response = requests.get('https://coffee.alexflipnote.dev/random.json')


@step('The returned image is correct')
def step_impl(context):
    assert_is_not_none(context.response.content)
    coffee_image = open('random.jpg', 'wb')
    coffee_image.write(context.response.content)


@step('The returned JSON is correct')
def step_impl(context):
    url = context.response.json()["file"]
    print(url)
    assert_is_not_none(context.response.json()['file'])
    assert('https://coffee.alexflipnote.dev/' in context.response.json()['file'])
    coffee_image = wget.download(url)
    print(coffee_image)
