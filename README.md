# Unidefy -- substitute unicode for ascii equivalents, if available

I wrote this primarily to normalize certain data for searching, the problem is that
certain characters, like the `umlat`, are hard to do on a normal keyboard, and so most
people don't bother, so this module can be used on the indexed strings to allow
either a `u` or an `umlat` to be used (since the `u` wouldn't be changed and the `umlat` would
be changed to the `u`) so you can search both ways but only have to store one version.

There are other modules that help with this, but python's builtin `unicodedata` didn't quite
do what I needed since it only uses defined [unicode normalizations](http://en.wikipedia.org/wiki/Unicode_normalization),
and something like [unidecode](https://pypi.python.org/pypi/Unidecode) works
but it's a little too eager, getting rid of unicode chars it doesn't recognize. I wanted to keep unicode that there wasn't
a good substitution for, likewise, I didn't really want to turn chinese characters into english
either (something `unidecode` does), it's definitely worth a look if you want more aggressive substitution.

To install, use Pip:

    pip install git+https://github.com/Jaymon/unidefy#egg=unidefy

## More reading, if you're interested

This is a dump of all the links I had open/used while I wrote this module

http://stackoverflow.com/questions/12944678/using-unicodedata-normalize-in-python-2-7

http://code.activestate.com/recipes/251871/

http://stackoverflow.com/questions/816285/where-is-pythons-best-ascii-for-this-unicode-database


http://lexsrv3.nlm.nih.gov/LexSysGroup/Projects/lvg/current/docs/designDoc/UDF/unicode/unicode.html

http://lexsrv3.nlm.nih.gov/LexSysGroup/Projects/lvg/current/docs/designDoc/UserContribution/index.html

http://lexsrv3.nlm.nih.gov/LexSysGroup/Projects/lvg/current/docs/designDoc/UDF/unicode/

http://search.cpan.org/~sburke/Text-Unidecode-0.04/lib/Text/Unidecode.pm


http://www.tablix.org/~avian/blog/archives/2009/01/unicode_transliteration_in_python/

http://stackoverflow.com/questions/4808967/replacing-unicode-punctuation-with-ascii-approximations

http://stackoverflow.com/questions/138449/how-to-convert-a-unicode-character-to-its-ascii-equivalent

http://stackoverflow.com/questions/5651124/is-there-a-way-to-dumb-down-text-from-unicode-to-ascii

## I got the data for the substitution table from these locations

http://lexsrv3.nlm.nih.gov/LexSysGroup/Projects/lvg/current/docs/designDoc/UserContribution/asciiConversion.html

http://unicode.org/repos/cldr/trunk/common/transforms/Latin-ASCII.xml

http://lexsrv3.nlm.nih.gov/LexSysGroup/Projects/lvg/current/docs/designDoc/UDF/unicode/MapTables/CoreNormResults.html
















