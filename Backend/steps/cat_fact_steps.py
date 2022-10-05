from behave import step
from nose.tools import assert_equal, assert_is_not_none
import requests


@step('I send a GET request to fact')
def send_get_fact(context):
    context.response = requests.get('https://catfact.ninja/fact')


@step('I send a GET request to facts')
def send_get_fact(context):
    context.response = requests.get('https://catfact.ninja/facts')


@step('I send a GET request to breeds')
def send_get_fact(context):
    context.response = requests.get('https://catfact.ninja/breeds')


@step('the API returns response {status_code}')
def send_get_fact(context, status_code):
    assert_equal(context.response.status_code, int(status_code))


@step('The returned data is correct')
def send_get_fact(context):
    assert_is_not_none(context.response.json()['fact'])
    assert_equal(str, type(context.response.json()['fact']))
    assert_equal(int, type(context.response.json()['length']))
    assert_equal(len(context.response.json()['fact']), context.response.json()['length'])


@step('The list of facts is returned')
def send_get_fact(context):
    for fact in context.response.json()['data']:
        assert_is_not_none(fact['fact'])
        assert_equal(str, type(fact['fact']))
        assert_equal(int, type(fact['length']))
        assert_equal(len(fact['fact']), fact['length'])


@step('The list of breeds is returned')
def send_get_fact(context):
    for breed in context.response.json()['data']:
        assert_is_not_none(breed['breed'])
        assert_is_not_none(breed['country'])
        assert_is_not_none(breed['origin'])
        assert_is_not_none(breed['coat'])
        assert_is_not_none(breed['pattern'])
        assert_equal(str, type(breed['breed']))
        assert_equal(str, type(breed['country']))
        assert_equal(str, type(breed['origin']))
        assert_equal(str, type(breed['coat']))
        assert_equal(str, type(breed['pattern']))
