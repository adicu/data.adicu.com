import test_shunt

# it's ok to import lib files and test them directly
# application code should be tested end-to-end with http calls

# py.test allows you to generate a lot of test parameters to the same test
# for example, write one test that checks for proper handling of invalid input
# and then parameterize all sorts of invalid input

def pytest_generate_tests(metafunc):
    # this is called once for each function
    # you call metafunc.addcall() appropriately to add extra executions of the test function
    if metafunc.function == test_app:
        for i in range(2):
            metafunc.addcall(funcargs=dict(days=i))

def test_app(days):
    # just use assertions to do tests
    # it's ok to build generic fuctions that test a common bit of functionality
    # and use those functions in lots of different tests (ie: a generic http_get that asserts response.code == 200)
    # in tests print or log output liberally; py.test will only show output when a test fails
    assert isinstance(days, int)
