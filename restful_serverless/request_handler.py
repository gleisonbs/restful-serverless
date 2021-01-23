class RequestHandler:
    def __init__(self):
        self._route_prefix = ""

    def add_route(self, url, handler):
        ...

    def route_prefix(self, prefix):
        self._route_prefix = prefix
