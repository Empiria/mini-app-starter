import m3
from app.services import frame

from ._anvil_designer import HelloWorldTemplate

header_content = """
I'm a mini-app starter kit written (almost) entirely in Python!
"""
source_code_content = """
My source code is available on [radicle](git@github.com:Empiria/mini-app-starter.git) or, if you insist, on [github](https://github.com/empiria/mini-app-starter) too.
"""
anvil_content = """
I was created using the [Anvil](https://anvil.works) framework.
If you have an Anvil account, you can [clone](https://anvil.works/build#clone:PULS75XJLCWFIACD=DE3LKNF7IJER4OJWUZNRTMO6) me on there.
"""

authors = [
    {"handle": "meatballs", "fid": 484396},
    {"handle": "theref", "fid": 344568},
]

class HelloWorld(HelloWorldTemplate):
    def __init__(self, **properties):
        self.header_text.content = header_content
        self.source_code_text.content = source_code_content
        self.anvil_text.content = anvil_content
        for author in authors:
            button = m3.components.Button(text=f"@{author['handle']}", appearance="text")
            button.tag.fid = author["fid"]
            button.add_event_handler("click", self.click_author_link)
            self.authors_flow_panel.add_component(button)
        self.init_components(**properties)

    def click_author_link(self, sender, **event_args):
        frame.view_profile(sender.tag.fid)
