"""
Lazy Requests Testing module.
"""

KEY = "SOME_KEY"
ORGANIZATION_ID = "ORGANIZATION_ID"
ADMIN_ID = "ADMIN_ID"

import sys
import unittest
try:
    from unittest import mock
except ImportError:
    # backup for python2
    import mock

# The context.py file on this folder sets up the context for the test case.
from context import LazyRequests, build_mocked_requests_decorator

URL = "https://meraki.dashboard.api"
HEADERS = {"Content-Type": "application/json"}
DATA = {}
RESPONSE = {"something": "cool"}

class TestMerakiApi(unittest.TestCase):
    """ Lazy Requests test case. """

    methods = ["get", "post", "put", "delete"]

    def setUp(self):
        self.lazy_request = LazyRequests(URL, HEADERS, DATA)

    def test_save_url(self):
        """ Should save the url after invoked. """
        self.assertEqual(self.lazy_request.url, URL)

    def test_save_headers(self):
        """ Should save the headers after invoked. """
        self.assertEqual(self.lazy_request.headers, HEADERS)

    def test_save_data(self):
        """ Should save the data after invoked. """
        self.assertEqual(self.lazy_request.data, DATA)

    def test_cache(self):
        """ A function should get cached. """
        def test_check(method):
            """ Check if the LazyRequests method caches a function. """
            lazy_request = LazyRequests(URL, HEADERS, DATA)
            self.assertIsNone(lazy_request.cached)
            request_method = getattr(lazy_request, method, None)
            request_method()
            self.assertTrue(callable(lazy_request.cached))
        # Run for each method
        map(test_check, self.methods)

    def check_test_call(self, result, mocked, expected_args={}):
        """ Helper function used to test call() method. """
        self.assertEqual(result, RESPONSE)
        if not expected_args:
            expected_args = {
                "url": URL,
                "headers": HEADERS,
                "data": DATA
            }
        actual_args = mocked.call_args_list[0][1]
        actual_args["url"] = URL
        self.assertEqual(expected_args, actual_args)

    @mock.patch(
        "requests.get"
        , side_effect=build_mocked_requests_decorator(URL, RESPONSE)
    )
    def test_get_call(self, mocked=None):
        """
        Should call the appropiate requests function of raise an Exception.
        """
        result = self.lazy_request.get().call().json()
        expected_args = {
            "url": URL,
            "headers": HEADERS,
            "params": DATA
        }
        self.check_test_call(result, mocked, expected_args)

    @mock.patch(
        "requests.post"
        , side_effect=build_mocked_requests_decorator(URL, RESPONSE)
    )
    def test_post_call(self, mocked=None):
        """
        Should call the appropiate requests function of raise an Exception.
        """
        result = self.lazy_request.post().call().json()
        self.check_test_call(result, mocked)

    @mock.patch(
        "requests.put"
        , side_effect=build_mocked_requests_decorator(URL, RESPONSE)
    )
    def test_put_call(self, mocked=None):
        """
        Should call the appropiate requests function of raise an Exception.
        """
        result = self.lazy_request.put().call().json()
        self.check_test_call(result, mocked)

    @mock.patch(
        "requests.delete"
        , side_effect=build_mocked_requests_decorator(URL, RESPONSE)
    )
    def test_delete_call(self, mocked=None):
        """
        Should call the appropiate requests function of raise an Exception.
        """
        result = self.lazy_request.delete().call().json()
        self.check_test_call(result, mocked)

if __name__ == '__main__':
    unittest.main()
