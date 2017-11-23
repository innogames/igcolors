"""
Functions for wrapping strings in ANSI color codes.

Each function within this module returns the input string ``text``, wrapped
with ANSI color codes for the appropriate color.

For example, to print some text as green on supporting terminals::

    from igcolors import green

    print(green("This text is green!"))

Because these functions simply return modified strings, you can nest them::

    from igcolors import red, green

    print(red("This sentence is red, except for " + \
          green("these words, which are green") + "."))

If ``bold`` is set to ``True``, the ANSI flag for bolding will be flipped on
for that particular invocation, which usually shows up as a bold or brighter
version of the original color on most terminals.
Else If ``dim`` is set to ``True``, the ANSI flag for dim will be flipped on
for that particular invocation, which usually shows up as a bold or brighter
version of the original color on most terminals.
"""


def _wrap_with(code):

    def inner(text, light=False, bold=False, dim=False, underline=False,
              blink=False, reverse=False, hidden=False):
        c = code
        if light:
            c = str(int(c)+60)
        if bold:
            c = "1;%s" % c
        if dim:
            c = "2;%s" % c
        if underline:
            c = "4;%s" % c
        if blink:
            c = "5;%s" % c
        if reverse:
            c = "7;%s" % c
        if hidden:
            c = "8;%s" % c

        return "\033[%sm%s\033[0m" % (c, text)
    return inner


gray = _wrap_with('30')
red = _wrap_with('31')
green = _wrap_with('32')
yellow = _wrap_with('33')
blue = _wrap_with('34')
magenta = _wrap_with('35')
cyan = _wrap_with('36')
white = _wrap_with('37')
