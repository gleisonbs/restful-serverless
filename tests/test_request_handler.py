from unittest import TestCase

from restful_serverless import request_handler
from restful_serverless.endpoint import Endpoint
from restful_serverless.request_handler import RequestHandler


def make_endpoint():
    class TestEndpoint(Endpoint):
        ...

    return TestEndpoint()


def make_sut():
    return RequestHandler()


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

        add_route = make_sut().add_route
        self.assertEqual(
            hasattr(add_route, "__call__"),
            True,
            "RequestHandler: add_route is not callable",
        )

    def test_add_route_receives_two_parameters(self):
        add_route = make_sut().add_route
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

        route_prefix = make_sut().route_prefix
        self.assertEqual(
            hasattr(route_prefix, "__call__"),
            True,
            "RequestHandler: route_prefix is not callable",
        )

    def test_route_prefix_receives_two_parameters(self):
        route_prefix = make_sut().route_prefix
        self.assertEqual(
            route_prefix.__code__.co_argcount,
            1 + 1,
            "RequestHandler: route_prefix should accept two parameters "
            "(including self)",
        )

    def test_has__route_prefix_str_property(self):
        rh = make_sut()
        self.assertEqual(
            rh._route_prefix,
            "",
            "RequestHandler: _route_prefix should be and empty string",
        )

    def test_route_prefix_method_sets__route_prefix_property(self):
        rh = make_sut()
        rh.route_prefix("/api")
        self.assertEqual(
            rh._route_prefix,
            "/api",
            "RequestHandler: route_prefix is not setting _route_prefix",
        )

    def test_route_prefix_raises_when_parameter_is_incorrect(self):
        rh = make_sut()
        with self.assertRaisesRegex(
            ValueError,
            "route_prefix Invalid argument for prefix parameter, "
            "must be string",
        ):
            rh.route_prefix(None)
        with self.assertRaisesRegex(
            ValueError,
            "route_prefix Invalid argument for prefix parameter, "
            "must be string",
        ):
            rh.route_prefix(4321)

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

    def test_has__endpoints_dict_property(self):
        rh = make_sut()
        self.assertEqual(
            rh._endpoints,
            {},
            "RequestHandler: _endpoints should be and empty dictionary",
        )

    def test_add_route_creates_correct_entry_in_endpoint_dict(self):
        rh = make_sut()
        test_endpoint = make_endpoint()

        self.assertEqual(len(rh._endpoints), 0)
        rh.add_route("/", test_endpoint)
        self.assertEqual(len(rh._endpoints), 1)
        self.assertEqual(rh._endpoints["/"], test_endpoint)

    def test_add_route_raises_when_route_already_in_endpoints(self):
        rh = make_sut()
        rh.add_route("/", make_endpoint())
        with self.assertRaisesRegex(
            ValueError,
            "add_route: route already added",
        ):
            rh.add_route("/", make_endpoint())
