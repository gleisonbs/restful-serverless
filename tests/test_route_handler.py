from unittest import TestCase

from werkzeug.routing import Map

from restful_serverless import route_handler
from restful_serverless.route_handler import RouteHandler


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

    def test_has__urls_Map_property(self):
        rh = make_sut()
        self.assertEqual(
            hasattr(rh, "_urls"),
            True,
            "RouteHandler: has no _urls attribute",
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

    # CALLABLES ACCEPTS CORRECT NUMBER OF PARAMETERS
    def test_add_receives_one_parameter(self):
        add = make_sut().add
        self.assertEqual(
            add.__code__.co_argcount,
            1 + 1,
            "RouteHandler: add should accept two parameters"
            "(including self)",
        )

    # CALLABLES SET PROPERTIES
    def test_add_creates_correct_entry_in_rules(self):
        rh = make_sut()

        self.assertEqual(len(rh._rules._rules), 0)
        rh.add("/<int:year>")
        self.assertEqual(len(rh._rules._rules), 1)

    def test_parse_route_correctly_parses_route(self):
        rh = make_sut()
        rh.add("/api/user/<int:id>")

        route, parameters = rh.parse("/api/user/43")
        self.assertEqual(route, "/api/user/<int:id>")
        self.assertEqual(parameters, {"id": 43})
