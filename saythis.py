#!/usr/bin/env python
# -*- coding: utf-8 -*-


DEFAULT_LANGUAGE = 'en'
DEFAULT_TEMP_FILE = '/tmp/test.mp3'
DEFAULT_PLAY_COMMAND = 'mplayer %s'

import sys
import os
import click
import urllib
from zenlog import log

lang = 'pt'


class AppURLopener(urllib.FancyURLopener):
    # we create a custom URL opener because Google only accepts Mozilla user agents
    version = "Mozilla"
urllib._urlopener = AppURLopener()

if not len(sys.argv) > 1:
    print "I need a string to speak!"
    sys.exit()

saythis = sys.argv[1]


def text_to_mp3(text, outfile, lang):
    url = "http://translate.google.com/translate_tts?ie=UTF-8&q=%s&tl=%s&prev=input" % (urllib.quote(saythis), lang)
    try:
        urllib.urlretrieve(url, outfile)
    except IOError:
        log.error('Got IOError -- are you online?')
        raise


@click.command()
@click.option("-l", "--lang", help="Language to read the text in", default="en")
@click.option("-o", "--outfile", help="Save to an MP3 file instead of playing it", type=click.Path())
@click.argument("text")
def run(text, outfile, lang):
    speak = False
    if not outfile:
        outfile = DEFAULT_TEMP_FILE
        speak = True

    text_to_mp3(text, outfile, lang)
    if speak:
        os.system(DEFAULT_PLAY_COMMAND % outfile)
        os.remove(outfile)

if __name__ == '__main__':
    run()
