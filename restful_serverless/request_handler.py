from restful_serverless.endpoint import Endpoint
from restful_serverless.route_handler import RouteHandler


class RequestHandler:
    def __init__(self, route_handler):
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

        self._route_handler.add(route, handler)

    def prefix_routes(self, prefix):
        if not isinstance(prefix, str):
            raise ValueError(
                "prefix_routes Invalid argument for prefix parameter, "
                "must be string"
            )

        self._route_handler.prefix(prefix)
