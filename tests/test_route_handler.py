from unittest import TestCase

from werkzeug.routing import Map

from restful_serverless import route_handler
from restful_serverless.endpoint import Endpoint
from restful_serverless.route_handler import RouteHandler


def make_endpoint():
    class EndpointStub(Endpoint):
        ...

    return EndpointStub()


def make_sut():
    return RouteHandler()


class TestRouteHandler(TestCase):
    # HAS ROUTE HANDLER CLASS
    def test_route_handler_exists(self):
        self.assertEqual(
            hasattr(route_handler, "RouteHandler"),
            True,
            "route_handler: no RouteHandler attribute found",
        )

    # ROUTE HANDLER CLASS HAS PROPERTIES
    def test_has__prefix_str_property(self):
        rh = make_sut()
        self.assertEqual(
            rh._prefix,
            "",
            "RouteHandler: _prefix should be and empty string",
        )

    def test_has__route_prefix_str_property(self):
        rh = make_sut()
        self.assertEqual(
            rh._prefix,
            "",
            "RouteHandler: _route_prefix should be and empty string",
        )

    def test_has__endpoints_dict_property(self):
        rh = make_sut()
        self.assertEqual(
            rh._endpoints,
            {},
            "RouteHandler: _endpoints should be and empty dictionary",
        )

    def test_has__rules_Map_property(self):
        rh = make_sut()
        self.assertEqual(
            hasattr(rh, "_rules"),
            True,
            "RouteHandler: has no _rules attribute",
        )

        self.assertIsInstance(
            rh._rules,
            Map,
            "RouteHandler: _rules is not a werkzeug Map",
        )

    # ROUTE HANDLER CLASS HAS CALLABLES
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

    # CALLABLES ACCEPTS CORRECT NUMBER OF PARAMETERS
    def test_add_receives_two_parameters(self):
        add = make_sut().add
        self.assertEqual(
            add.__code__.co_argcount,
            2 + 1,
            "RouteHandler: add should accept three parameters"
            "(including self)",
        )

    def test_prefix_receives_one_parameter(self):
        prefix = make_sut().prefix
        self.assertEqual(
            prefix.__code__.co_argcount,
            1 + 1,
            "RouteHandler: prefix should accept two parameters"
            "(including self)",
        )

    # CALLABLES SET PROPERTIES
    def test_prefix_method_sets_prefix_property(self):
        rh = make_sut()
        rh.prefix("/api")
        self.assertEqual(
            rh._prefix,
            "/api",
            "RouteHandler: prefix method not setting _prefix",
        )

    def test_prefix_method_sets__prefix_property(self):
        rh = make_sut()
        rh.prefix("/api")
        self.assertEqual(
            rh._prefix,
            "/api",
            "RouteHandler: prefix method not setting _prefix",
        )

    def test_add_creates_correct_entry_in_endpoints(self):
        rh = make_sut()
        test_endpoint = make_endpoint()

        self.assertEqual(len(rh._endpoints), 0)
        rh.add("/", test_endpoint)
        self.assertEqual(len(rh._endpoints), 1)
        self.assertEqual(rh._endpoints["/"], test_endpoint)

    def test_add_route_adds_with_prefix(self):
        rh = make_sut()
        rh.add("/", make_endpoint())
        self.assertIn("/", rh._endpoints.keys())

        rh.prefix("/api")
        rh.add("/users", make_endpoint())
        self.assertIn("/api/users", rh._endpoints.keys())
