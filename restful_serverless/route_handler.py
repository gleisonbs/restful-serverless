from os import path

from werkzeug.routing import Map, Rule


class RouteHandler:
    def __init__(self):
        self._prefix = ""
        self._endpoints = {}
        self._rules = Map()
        self._urls = self._rules.bind("/")

    def add(self, route, handler):
        if self._prefix and route.startswith("/"):
            route = route[1:]

        route_with_prefix = path.join(self._prefix, route)
        self._endpoints[route_with_prefix] = handler
        self._rules.add(Rule(route_with_prefix, endpoint=route_with_prefix))

    def prefix(self, _prefix):
        self._prefix = _prefix

    def parse(self, route):
        res = self._urls.match(route)
        return res
