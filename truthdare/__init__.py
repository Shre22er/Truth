
from .truth import Truth


def setup(bot):
    n = Truth()
    bot.add_cog(n)