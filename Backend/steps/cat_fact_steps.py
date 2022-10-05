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
