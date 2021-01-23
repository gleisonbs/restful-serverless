class Endpoint:
    ...


class RequestHandler:
    def __init__(self):
        self._route_prefix = ""
        self._endpoints = {}

    def add_route(self, url, route_handler):
        if not isinstance(url, str):
            raise ValueError(
                "add_route: Invalid argument for url parameter, "
                "must be string"
            )

        if not isinstance(route_handler, Endpoint):
            raise ValueError(
                "add_route: Invalid argument for route_handler parameter, "
                "must be Endpoint"
            )

    def route_prefix(self, prefix):
        if not isinstance(prefix, str):
            raise ValueError(
                "route_prefix Invalid argument for prefix parameter, "
                "must be string"
            )
        self._route_prefix = prefix
