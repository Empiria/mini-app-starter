from routing import router
import json


class HelloRoute(router.Route):
    path = "/home"
    form = "app.HelloWorld"

    def meta(self, **kwargs):
        return {
            "title": "Hello World",
            "description": "Mini App Python Starter Kit",
            "fc:frame": json.dumps(embed),
        }
