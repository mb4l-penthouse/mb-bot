#!/usr/bin/env python3

import config
import sys

from mbot import MBot

def usage_hint():
    s = "\n" +\
        "usage:\n" +\
        "  $ ./run.py <config>\n" +\
        "\n" +\
        "example:\n" +\
        "  $ ./run.py cfg/example.json"
    return s

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(usage_hint())
        sys.exit(0)

    cfg = config.load_cfg(sys.argv[1])
    bot = MBot()
    bot.run(cfg["TOKEN"])
