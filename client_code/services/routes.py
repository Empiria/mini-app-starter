from routing import router
import json

embed = {
    "version": "next",
    "imageUrl": "https://mini-app-starter.anvil.app/_/theme/warpcast.jpeg",
    "button": {
        "title": "🚩 Start",
        "action": {
            "type": "launch_frame",
            "url": "https://mini-app-starter.anvil.app",
            "name": "Mini App Starter",
            "splashImageUrl": "https://mini-app-starter.anvil.app/_/theme/warpast.jpeg",
            "splashBackgroundColor": "#f5f0ec"
        }
    }
}


class HomeRoute(router.Route):
    path = "/"
    form = "app.HelloWorld"


class HelloRoute(router.Route):
    path = "/home"
    form = "app.HelloWorld"

    def meta(self, **kwargs):
        return {
            "title": "Hello World",
            "description": "Mini App Python Starter Kit",
            "fc:frame": json.dumps(embed),
        }
