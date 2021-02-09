from restful_serverless.endpoint import Endpoint
from restful_serverless.request_handler import RequestHandler
from restful_serverless.route_handler import RouteHandler

route_hander = RouteHandler()
request_handler = RequestHandler(route_hander)


class User(Endpoint):
    ...


request_handler.prefix_routes("/api")
request_handler.add_route("/user/<int:id>", User())
print(route_hander.parse("/api/user/123"))
