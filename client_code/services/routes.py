from routing import router


class HelloRoute(router.Route):
    path = "/"
    form = "app.HelloWorld"
