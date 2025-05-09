from routing import router


class HelloRoute(router.Route):
    path = "/"
    form = "app.HelloWorld"

    def meta(self, **loader_args):
        return {"title": "Hello World", "description": "A farcaster mini app MWE", "fc:frame": "hello"}
