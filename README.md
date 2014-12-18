A multilanguage TTS courtesy of Google Translate
------------------------------------------------

This script uses Google Translate to do a simple text-to-speech operation. It
plays back the result by default when you run it:

    python saythis.py "Say this!"

Quotes can be omitted too:

    saythis.py Say this!

You can also specify the language:

    saythis.py "Pimbas!" --lang pt

Output to a file instead of playing it:

    saythis.py "Pimbas!" --lang pt --output pimbas.mp3

This is based on a handy [Lifehacker article](http://lifehacker.com/5426797/google-translate-url-generates-instant-text+to+speech-mp3-files
).


TODO 
----

* List available languages

License
-------

This script is copyright (C) Manufactura Independente 2011-2014.

Published under the terms of the [GNU General Public license](http://www.gnu.org/licenses/gpl.html).



