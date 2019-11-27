import asyncio
import logging

from discord.ext.commands import Bot

class MBot(Bot):
    def __init__(self,
                 command_prefix = "$",
                 logger = None,
                 **options):
        if logger is None:
            self._logger = self._make_default_logger()
        super(MBot, self).__init__(command_prefix=command_prefix)
        
    def _make_default_logger(self):
        logger = logging.getLogger("mbot")
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler(filename="mbot.log",
                                      encoding="utf-8",
                                      mode="w")
        formatstr = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
        handler.setFormatter(logging.Formatter(formatstr))
        logger.addHandler(handler)
        return logger
        
    async def on_ready(self):
        await self._logger.info("connected")
        
bot = MBot()

@bot.command(name="test")
async def test(ctx, arg):
    await ctx.send(arg)