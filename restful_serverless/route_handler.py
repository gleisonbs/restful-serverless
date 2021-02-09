from werkzeug.routing import Map, Rule


class RouteHandler:
    def __init__(self):
        self._prefix = ""
        self._rules = Map()
        self._urls = self._rules.bind("/")

    def add(self, route):
        self._rules.add(Rule(route, endpoint=route))

    def parse(self, route):
        res = self._urls.match(route)
        return res
