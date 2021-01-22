from unittest import TestCase

from restful_serverless import request_handler
from restful_serverless.request_handler import RequestHandler


class TestRequestHandler(TestCase):
    def test_request_handler_exists(self):
        self.assertEqual(
            hasattr(request_handler, "RequestHandler"),
            True,
            "request_handler has no RequestHandler attribute",
        )

    def test_request_handler_has_add(self):
        self.assertEqual(
            hasattr(RequestHandler, "add_route"),
            True,
            "RequestHandler has no add_route attribute",
        )

    def test_add_route_receives_two_parameters(self):
        add_route = RequestHandler().add_route
        self.assertEqual(add_route.__code__.co_argcount, 2)
