import anvil.server
from app.services import routes  # noqa unused_import


@anvil.server.wellknown_endpoint("/farcaster.json")
def manifest():
    _manifest = {
        # "accountAssociation": {
        #     "header": "Your header",
        #     "payload": "Your payload",
        #     "signature": "Your signature",
        # },
        "frame": {
            "version": "1",
            "name": "HelloWorld",
            "homeUrl": "https://mini-app-starter.anvil.app",
            "iconUrl": "https://mini-app-starter.anvil.app/_/theme/warpcast.jpeg",
        }
    }
    return _manifest