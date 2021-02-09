from os import path

from restful_serverless.endpoint import Endpoint
from restful_serverless.route_handler import RouteHandler


class RequestHandler:
    def __init__(self, route_handler):
        self._endpoints = {}
        self._prefix = ""

        if not isinstance(route_handler, RouteHandler):
            raise ValueError(
                "route_handler: Invalid argument for route parameter, "
                "must be RouteHandler"
            )

        self._route_handler = route_handler

    def add_route(self, route, handler):
        """Add a new route and a route handler.
        :param route: the route the handler will be mapped to
        :param handler: the Endpoint instance that will handle the route
        :returns: None
        :raises: ValueError
        """
        if not isinstance(route, str):
            raise ValueError(
                "add_route: Invalid argument for route parameter, "
                "must be string"
            )

        if not isinstance(handler, Endpoint):
            raise ValueError(
                "add_route: Invalid argument for route_handler parameter, "
                "must be Endpoint"
            )

        if self._prefix and route.startswith("/"):
            route = route[1:]

        route_with_prefix = path.join(self._prefix, route)
        self._endpoints[route_with_prefix] = handler
        self._route_handler.add(route_with_prefix)

    def prefix_routes(self, prefix):
        if not isinstance(prefix, str):
            raise ValueError(
                "prefix_routes Invalid argument for prefix parameter, "
                "must be string"
            )

        self._prefix = prefix

    def handle(self, request):
        self._route_handler.parse(request.path)
