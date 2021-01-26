from unittest import TestCase

from restful_serverless import route_handler
from restful_serverless.endpoint import Endpoint
from restful_serverless.route_handler import RouteHandler


def make_endpoint():
    class TestEndpoint(Endpoint):
        ...

    return TestEndpoint()


def make_sut():
    return RouteHandler()


class TestRouteHandler(TestCase):
    def test_request_handler_exists(self):
        self.assertEqual(
            hasattr(route_handler, "RouteHandler"),
            True,
            "route_handler: no RouteHandler attribute found",
        )
