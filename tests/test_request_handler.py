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
