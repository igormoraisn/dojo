from behave import step
from nose.tools import assert_equal


@step('the API returns response {status_code}')
def send_get_fact(context, status_code):
    assert_equal(context.response.status_code, int(status_code))
