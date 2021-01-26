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

    def test_route_handler_has_callable_add(self):
        self.assertEqual(
            hasattr(RouteHandler, "add"),
            True,
            "RouteHandler: no add attribute found",
        )

        add = make_sut().add
        self.assertEqual(
            hasattr(add, "__call__"),
            True,
            "RouteHandler: add is not callable",
        )

    def test_add_receives_two_parameters(self):
        add = make_sut().add
        self.assertEqual(
            add.__code__.co_argcount,
            2 + 1,
            "RouteHandler: add should accept three parameters"
            "(including self)",
        )

    def test_route_handler_has_callable_prefix(self):
        self.assertEqual(
            hasattr(RouteHandler, "prefix"),
            True,
            "RouteHandler: no prefix attribute found",
        )

        prefix = make_sut().prefix
        self.assertEqual(
            hasattr(prefix, "__call__"),
            True,
            "RouteHandler: prefix is not callable",
        )
