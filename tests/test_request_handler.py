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

    def test_request_handler_has_callable_add_route(self):
        self.assertEqual(
            hasattr(RequestHandler, "add_route"),
            True,
            "RequestHandler has no add_route attribute",
        )

        add_route = RequestHandler().add_route
        self.assertEqual(
            hasattr(add_route, "__call__"),
            True,
            "RequestHandler: add_route is not callable",
        )

    def test_add_route_receives_two_parameters(self):
        add_route = RequestHandler().add_route
        self.assertEqual(
            add_route.__code__.co_argcount,
            2 + 1,
            "RequestHandler: add_route should accept three parameters"
            "(including self)",
        )

    def test_request_handler_has_callable_route_prefix(self):
        self.assertEqual(
            hasattr(RequestHandler, "route_prefix"),
            True,
            "RequestHandler has no route_prefix attribute",
        )

        route_prefix = RequestHandler().route_prefix
        self.assertEqual(
            hasattr(route_prefix, "__call__"),
            True,
            "RequestHandler: route_prefix is not callable",
        )

    def test_route_prefix_receives_two_parameters(self):
        route_prefix = RequestHandler().route_prefix
        self.assertEqual(
            route_prefix.__code__.co_argcount,
            1 + 1,
            "RequestHandler: route_prefix should accept two parameters "
            "(including self)",
        )

    def test_has__route_prefix_property(self):
        rh = RequestHandler()
        self.assertEqual(
            rh._route_prefix,
            "",
            "RequestHandler: _route_prefix should be and empty string",
        )

    def test_route_prefix_method_sets__route_prefix_property(self):
        rh = RequestHandler()
        rh.route_prefix("/api")
        self.assertEqual(
            rh._route_prefix,
            "/api",
            "RequestHandler: route_prefix is not setting _route_prefix",
        )
