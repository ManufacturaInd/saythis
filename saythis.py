#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Saythis.py
#
# Multilanguage TTS courtesy of Google Translate
# (C) Manufactura Independente 2011
# Released under the terms of the GPL v3
#   http://www.gnu.org/licenses/gpl.html 
#
# Based on the hints given here:
# http://lifehacker.com/5426797/google-translate-url-generates-instant-text+to+speech-mp3-files
#
# Usage:
#   saythis.py "Say this!"
#
# Quotes can be omitted too:
#   saythis.py Say this!
#
# You can also specify the language:
#   saythis.py "Pimbas!" --lang pt
#
# Output to a file instead of playing it:
# 
#   saythis.py "Pimbas!" --lang pt --output pimbas.mp3
#
# TODO: 
# - List available languages

DEFAULT_LANGUAGE = 'en'
DEFAULT_TEMP_FILE = '/tmp/test.mp3'
DEFAULT_PLAY_COMMAND = 'mplayer %s'

import sys, os
import urllib

lang = 'pt'

# we create a custom URL opener because Google only accepts Mozilla user agents
class AppURLopener(urllib.FancyURLopener):
    version = "Mozilla"
urllib._urlopener = AppURLopener()

if not len(sys.argv) > 1:
    print "I need a string to speak!"
    sys.exit()

saythis = sys.argv[1]
def tts(saythis, outfile, lang):
    url = "http://translate.google.com/translate_tts?ie=UTF-8&q=%s&tl=%s&prev=input" % (urllib.quote(saythis), lang)
    try:
        urllib.urlretrieve (url, outfile)
    except IOError:
        print 'Received IOError -- are you online?'
        sys.exit()

if __name__ == '__main__':
    # analisar as opções da linha de comandos
    import optparse
    parser = optparse.OptionParser()
    parser.add_option('-l', '--lang', 
                      dest="lang", 
                      default="Specify language (default: en)",
                      help=''
                      )
    parser.add_option('-o', '--output', 
                      dest="output", 
                      default="",
                      help='Save to specified file (MP3 format) instead of playing a sound'
                      )
    options, remainder = parser.parse_args()
    lang = options.lang
    outfile = options.output
    saythis = ' '.join(remainder)

    if not outfile:
        outfile = DEFAULT_TEMP_FILE
        speak = True
    if not lang:
        lang = DEFAULT_LANGUAGE

    tts(saythis, outfile, lang)

    if speak:
        os.system(DEFAULT_PLAY_COMMAND % outfile)
        os.remove(outfile)
