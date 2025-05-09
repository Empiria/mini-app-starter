from routing import router

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


class HelloRoute(router.Route):
    path = "/"
    form = "app.HelloWorld"
