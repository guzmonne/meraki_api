"""
Sets the context to be able to run the tests.
"""

################################################################################
# This code was taken from "The hitchhiker guide to python".                   #
#                                                                              #
# - Use a simple path modification to resolve the package properly.            #
################################################################################
import os
import sys

sys.path.insert(
    0
    , os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), '..'
        )
    )
)
################################################################################
# Here we import the modules to be used on the tests.                          #
################################################################################
from meraki_api import MerakiAPI, LazyRequests
################################################################################
# This is a way to mock requests functions.                                    #
# It was taken from the following Stack Overflow answer by Johannes Fahrenkrug #
# https://stackoverflow.com/questions/15753390/                                #
# python-mock-requests-and-the-response                                        #
################################################################################
class MockResponse:
    """ Requests MockResponse class. """
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        """ Return the JSON data. """
        return self.json_data

def build_mocked_requests_decorator(url, response):
    """ Returns a method that can Mock a requests method. """
    def mocked_requests_method(*args, **kwargs):
        """ Returns a mocked response. """
        if args[0] == url:
            return MockResponse(response, 200)
        else:
            return MockResponse({
                "errors": "Invalid URL"
            }, 404)
    return mocked_requests_method
################################################################################
