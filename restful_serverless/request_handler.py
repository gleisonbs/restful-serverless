class RequestHandler:
    def __init__(self):
        self._route_prefix = ""

    def add_route(self, url, handler):
        ...

    def route_prefix(self, prefix):
        if not isinstance(prefix, str):
            raise ValueError(
                "route_prefix(prefix): Invalid argument for prefix parameter"
            )
        self._route_prefix = prefix
