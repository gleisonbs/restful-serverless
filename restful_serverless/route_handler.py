from os import path

from werkzeug.routing import Map


class RouteHandler:
    def __init__(self):
        self._prefix = ""
        self._endpoints = {}
        self._rules = Map()

    def add(self, route, handler):
        if self._prefix and route.startswith("/"):
            route = route[1:]

        route_with_prefix = path.join(self._prefix, route)
        self._endpoints[route_with_prefix] = handler

    def prefix(self, _prefix):
        self._prefix = _prefix
