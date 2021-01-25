from restful_serverless.endpoint import Endpoint


class RequestHandler:
    def __init__(self):
        self._route_prefix = ""
        self._endpoints = {}

    def add_route(self, route, route_handler):
        """Add a new route and a route handler.
        :param route: the route the handler will be mapped to
        :param route_handler: the Endpoint instance that will handle the route
        :returns: None
        :raises: ValueError
        """
        if not isinstance(route, str):
            raise ValueError(
                "add_route: Invalid argument for route parameter, "
                "must be string"
            )

        if not isinstance(route_handler, Endpoint):
            raise ValueError(
                "add_route: Invalid argument for route_handler parameter, "
                "must be Endpoint"
            )

        self._endpoints[route] = route_handler

    def route_prefix(self, prefix):
        if not isinstance(prefix, str):
            raise ValueError(
                "route_prefix Invalid argument for prefix parameter, "
                "must be string"
            )
        self._route_prefix = prefix
