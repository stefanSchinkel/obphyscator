#!/usr/bin/env python
""" ophyscator.py - a simple obfucation tool
"""

import numpy as np
import sys

HEAD = """
<ins>
<span style="display:inline;" id="ophyscator"></span>
<script type="text/javaScript">
"""

FOOT = """
document.getElementById('ophyscator').innerHTML = str;
</script>
<noscript>
<p>Sorry, you need to have JavaScript enabled to get the mail address</p>
</noscript>
</ins>
"""


def instructions(address, linkText):
    """ Print instructions
    """

    helpString = """
    =====================================================
    Include the code snipped from <ins> to </ins>in your
    page replacing <a href=mailto: ... </a> part.

    The `encrypted` email address is: {}
    and the link text is: {}
    =====================================================
    """
    print helpString.format(address, linkText)
    print cypherMail(address, linkText)


def cypherMail(mail, link):
    """ 'Encrypt' an email address given as a string
    and return an HTML/JS code snippet for embedding
    in a webpage.

    :arg email: email address to crypt
    :type email: <str>

    :arg link: link text to crypt
    :type link: <str>

    :return: JS string to embed in HTML
    :rtype: <str>
    """
    permMail = list(np.random.permutation(len(mail)))
    permLink = list(np.random.permutation(len(link)))

    #head
    js = HEAD + "var a = new Array("

    #JS variable for mail
    for idx in permMail:
        js += "'" + str(mail[idx]) + "',"
    js = js[:-1] + ");\n"

    #JS variable  for link
    js += "var b = new Array("
    for idx in permLink:
        js += "'" + str(link[idx]) + "',"
    js = js[:-1] + ");\n"

    # HTML mailto
    js += "var str = \"<a href='mailto:\"+"
    for idx in range(len(mail)):
        js += "a[" + str(permMail.index(idx)) + "]+"
    js += "\"'>\"+"

    # HTML link text
    for idx in range(len(link)):
        js += "b[" + str(permLink.index(idx)) + "]+"
    # js = js[:-1] + "+\"<\/a>\";\n"
    js = js[:-1] + "+\"</a>\";\n"

    # add closing
    js += FOOT

    return js

if __name__ == '__main__':

    nArgs = len(sys.argv)
    if nArgs <= 1:
        instructions("mail@example.com", "Click to send mail")
    elif nArgs <= 2:
        print cypherMail(sys.argv[1], sys.argv[1])
    else:
        print cypherMail(sys.argv[1], ' '.join(str(x) for x in sys.argv[2:]))
