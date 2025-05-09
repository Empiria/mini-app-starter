from ._anvil_designer import HelloWorldTemplate
import anvil.js

anvil.js.report_all_exceptions(True)

msg = """
I'm a mini-app starter kit created by @meatballs, @theref and @uglyfruitcake of [Empiria](https://www.empiria.co.uk).

I'm written (almost) entirely in Python using the [Anvil](https://anvil.works) framework.

My source code is available on [radicle](git@github.com:Empiria/mini-app-starter.git) or, if you insist, on [github](https://github.com/empiria/mini-app-starter) too.

If you have an Anvil account, you can [clone](https://anvil.works/build#clone:PULS75XJLCWFIACD=DE3LKNF7IJER4OJWUZNRTMO6) me on there.
"""


class HelloWorld(HelloWorldTemplate):
    def __init__(self, **properties):
        self.readme.content = msg
        self.init_components(**properties)
