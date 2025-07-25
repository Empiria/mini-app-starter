import m3
from app.services import frame

from ._anvil_designer import HelloWorldTemplate

header_content = """
I'm a mini-app starter kit written (almost) entirely in Python!
"""
source_code_content = """
You'll probably need to use a right mouse click to follow these links...

My source code is available on [radicle](https://app.radicle.xyz/nodes/rosa.radicle.xyz/rad:ztTFriaB1yVqcLR1WPcMZDfeKdbE) or, if you insist, on [github](https://github.com/empiria/mini-app-starter) too.

I was created using the [Anvil](https://anvil.works) framework.
If you have an Anvil account, you can [clone](https://anvil.works/build#clone:PULS75XJLCWFIACD=DE3LKNF7IJER4OJWUZNRTMO6) me on there.
"""

authors = {
    "meatballs": 484396,
    "theref": 344568,
    "uglyfruitcake": 1077524,
}

class HelloWorld(HelloWorldTemplate):
    def __init__(self, **properties):
        self.header_text.content = header_content
        self.source_code_text.content = source_code_content
        for nick, fid in authors.items():
            button = m3.components.Button(text=f"@{nick}", appearance="text")
            button.tag.fid = fid
            button.add_event_handler("click", self.click_author_link)
            self.authors_flow_panel.add_component(button)
        self.init_components(**properties)

    def click_author_link(self, sender, **event_args):
        frame.view_profile(sender.tag.fid)
