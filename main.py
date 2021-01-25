from werkzeug.routing import Map, Rule

m = Map(
    [
        Rule("/", endpoint="index"),
        Rule("/downloads/", endpoint="downloads/index"),
        Rule("/downloads/<int:id>", endpoint="downloads/show"),
        Rule("/user/<int:id>", endpoint="/user/<int:id>"),
    ]
)

urls = m.bind("/")

routes = ["/", "/downloads/42", "user/123"]
for r in routes:
    res = urls.match(r)
    print(res)
