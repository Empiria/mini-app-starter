from ._anvil_designer import HelloWorldTemplate
import anvil.js

anvil.js.report_all_exceptions(True)

msg = """
I'm a mini-app starter kit created by @meatballs, @theref and @uglyfruitcake of [Empiria](https://www.empiria.co.uk).

I'm written (almost) entirely in Python using the [Anvil](https://anvil.works) framework.

My source code is available on radicle or, if you insist, on github too.

If you have an Anvil account, you can clone me.
"""


class HelloWorld(HelloWorldTemplate):
    def __init__(self, **properties):
        self.readme.content = msg
        self.init_components(**properties)