#!/usr/bin/env python

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
<p>Sorry, you need to have JavaScript enabled to get the mail address</p></noscript>
</ins>
    """

def instructions(address, linkText):
    s = """
    =====================================================
    Include the code snipped below in your HTML replacing
    the whole <a href=mailto: ... </> part.
    The `encrypted` email address is:
    {}
    and the link text is:
    {}
    =====================================================
    """
    print s.format(address, linkText)

def cypherMail(mail, link):
    """ `Encrypt` an email address given as a string
    and return an JS code snippet for embedding in HTML

    :arg email: email address to crypt
    :type email: <str>

    :arg link: link text to crypt
    :type link: <str>

    :return: JS string to embed in HTML
    :rtype: <str>
    """
    permMail = list(np.random.permutation(len(mail)))
    permLink = list(np.random.permutation(len(link)))

    #incl  intro
    js = HEAD
    #JS variable for mail
    js += "var a = new Array("
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
    js = js[:-1] + '+"<\/a>";\n'

    # add closing
    js += FOOT

    return js

if __name__ == '__main__':

    if len(sys.argv) <= 1:
        address = "mail@example.com"
        linkText = "Click to send mail"

    else:
        try:
            address = sys.argv[1]
        except IndexError:
            print "interesting"
            sys.exit(-1)
        try:
            linkText = sys.argv[2]
        except IndexError:
            linkText = address

    #show  instructions
    instructions(address, linkText)

    print cypherMail(address, linkText)
