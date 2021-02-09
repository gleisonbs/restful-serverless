from unittest import TestCase

from mock import patch

from restful_serverless import request_handler
from restful_serverless.endpoint import Endpoint
from restful_serverless.request_handler import RequestHandler
from restful_serverless.route_handler import RouteHandler


def make_endpoint():
    class EndpointStub(Endpoint):
        ...

    return EndpointStub()


def make_route_handler():
    class RouteHandlerStub(RouteHandler):
        ...

    return RouteHandlerStub()


def make_sut():
    route_handler_stub = make_route_handler()
    return RequestHandler(route_handler_stub)


class TestRequestHandler(TestCase):
    #
    def test_request_handler_exists(self):
        self.assertEqual(
            hasattr(request_handler, "RequestHandler"),
            True,
            "request_handler has no RequestHandler attribute",
        )

    # REQUEST HANDLER CLASS HAS PROPERTIES
    def test_has__route_handler_str_property(self):
        rh = make_sut()
        self.assertEqual(
            hasattr(rh, "_route_handler"),
            True,
            "RequestHandler: has no _route_handler attribute",
        )

    def test_has__endpoints_dict_property(self):
        rh = make_sut()
        self.assertEqual(
            rh._endpoints,
            {},
            "RequestHandler: _endpoints should be and empty dictionary",
        )

    # REQUEST HANDLER CLASS HAS CALLABLES
    def test_request_handler_has_callable_add_route(self):
        self.assertEqual(
            hasattr(RequestHandler, "add_route"),
            True,
            "RequestHandler: no add_route attribute found",
        )

        add_route = make_sut().add_route
        self.assertEqual(
            hasattr(add_route, "__call__"),
            True,
            "RequestHandler: add_route is not callable",
        )

    def test_request_handler_has_callable_prefix_routes(self):
        self.assertEqual(
            hasattr(RequestHandler, "prefix_routes"),
            True,
            "RequestHandler no prefix_routes attribute found",
        )

        prefix_routes = make_sut().prefix_routes
        self.assertEqual(
            hasattr(prefix_routes, "__call__"),
            True,
            "RequestHandler: prefix_routes is not callable",
        )

    # CALLABLES ACCEPTS CORRECT NUMBER OF PARAMETERS
    def test_add_route_receives_two_parameters(self):
        add_route = make_sut().add_route
        self.assertEqual(
            add_route.__code__.co_argcount,
            2 + 1,
            "RequestHandler: add_route should accept three parameters"
            "(including self)",
        )

    def test_prefix_routes_receives_two_parameters(self):
        prefix_routes = make_sut().prefix_routes
        self.assertEqual(
            prefix_routes.__code__.co_argcount,
            1 + 1,
            "RequestHandler: prefix_routes should accept two parameters "
            "(including self)",
        )

    def test_constructor_accepts_one_parameter(self):
        sut = make_sut()
        self.assertEqual(
            hasattr(sut, "__init__"),
            True,
            "RequestHandler: no constructor found",
        )

        self.assertEqual(
            sut.__init__.__code__.co_argcount,
            1 + 1,
            "RequestHandler: __init__ should accept two parameters "
            "(including self)",
        )

    # CALLABLES SET PROPERTIES
    def test_constructor_sets_route_handler(self):
        route_handler = make_route_handler()
        sut = RequestHandler(route_handler)
        self.assertEqual(
            sut._route_handler,
            route_handler,
            "RequestHandler: "
            "_route_handler is different from the route_handler provided",
        )

    # CALLABLES RAISE WHEN CALLED WITH WRONG PARAMETERS
    def test_prefix_routes_raises_when_parameter_is_incorrect(self):
        rh = make_sut()
        with self.assertRaisesRegex(
            ValueError,
            "prefix_routes Invalid argument for prefix parameter, "
            "must be string",
        ):
            rh.prefix_routes(None)
        with self.assertRaisesRegex(
            ValueError,
            "prefix_routes Invalid argument for prefix parameter, "
            "must be string",
        ):
            rh.prefix_routes(4321)

    def test_add_route_raises_when_parameter_are_incorrect(self):
        rh = make_sut()
        with self.assertRaisesRegex(
            ValueError,
            "add_route: Invalid argument for route parameter, must be string",
        ):
            rh.add_route(None, None)
        with self.assertRaisesRegex(
            ValueError,
            "add_route: Invalid argument for route_handler parameter, "
            "must be Endpoint",
        ):
            rh.add_route("", None)

    def test_request_handler_raises_when_wrong_type_route_handler(self):
        with self.assertRaisesRegex(
            ValueError,
            "route_handler: Invalid argument for route parameter, "
            "must be RouteHandler",
        ):
            RequestHandler("route_handler")

    # CALLABLES CALL ROUTE HANDLER WITH CORRECT PARAMETERS
    def test_add_route_calls_add(self):
        sut = make_sut()
        route_handler = sut._route_handler
        test_route = "/test_route"
        test_endpoint = make_endpoint()

        with patch.object(
            route_handler, "add", wraps=route_handler.add
        ) as wrapped_add:
            sut.add_route(test_route, test_endpoint)
            wrapped_add.assert_called_with(test_route)

    def test_add_route_adds_with_prefix(self):
        rh = make_sut()
        rh.add_route("/", make_endpoint())
        self.assertIn("/", rh._endpoints.keys())

        rh.prefix_routes("/api")
        rh.add_route("/users", make_endpoint())
        self.assertIn("/api/users", rh._endpoints.keys())

    def test_add_creates_correct_entry_in_endpoints(self):
        rh = make_sut()
        test_endpoint = make_endpoint()

        self.assertEqual(len(rh._endpoints), 0)
        rh.add_route("/", test_endpoint)
        self.assertEqual(len(rh._endpoints), 1)
        self.assertEqual(rh._endpoints["/"], test_endpoint)
