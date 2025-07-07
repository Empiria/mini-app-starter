import anvil.server
import anvil.secrets
from app.services import routes  # noqa unused_import


@anvil.server.wellknown_endpoint("/farcaster.json")
def manifest():
    _manifest = {
        "accountAssociation": {
            "header": anvil.secrets.get_secret("fc-header"),
            "payload": anvil.secrets.get_secret("fc-payload"),
            "signature": anvil.secrets.get_secret("fc-signature"),
        },
        "frame": {
            "version": "1",
            "name": "HelloWorld",
            "homeUrl": "https://mini-app-starter.anvil.app/home",
            "iconUrl": "https://mini-app-starter.anvil.app/_/theme/warpcast.jpeg",
        }
    }
    return _manifest
