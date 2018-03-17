# -*- coding: utf-8 -*-

"""Main module."""

import emoji
import os


_, columns = os.popen('stty size', 'r').read().split()


def char_line(symbol):
    print(symbol * int(columns))


def emoji_line(symbol):
    """
    Try using emojis to make your debugging experience less miserable.
    Go check the emoji cheat sheet: https://www.webpagefx.com/tools/emoji-cheat-sheet
    """
    print((emoji.emojize(symbol, use_aliases=True) + " ") * int((int(columns) / 2)))

