Style-optimizations require low-specificity in content - use WikiText
markup as much as possible.[^1]

### Gingah

-   If site is down, it's potentially to patch Meltdown and Spectre
    flaws in processors - but daily, weekly, biweekly, and
    snapshot-backups are enabled on Linode, so the entire site should be
    redundantly safe
-   Custom SCSS at
    [MediaWiki:Custom.scss](MediaWiki:Custom.scss "wikilink") -
    live-parsed, debug at <https://swataftermath.com/scss/>
-   Searching for media in VisualEditor is very sensitive - but for
    example "tooltip" or "tool\*" (wildcard at the end) works.

#### GhostGraz

-   Previous instructions: <http://archive.is/jPqjV>
-   Working for 1.29, 1.30:
    <https://github.com/MisterVector/gproxy-ghostgraz>
    -   This will compile, apparently.

### Jamie

-   Move pages from swatam.wikispaces.com
-   Update page formatting to conform with WikiMedia vs WikiSpaces
-   Update content of pages

### Alex

-   Update content of pages

### Resources:

-   DokuWiki Zip: <http://gingahmail.com/pages.zip>
-   You can use {{Anchor\|Chem._Reliant\|Chem_Reliant\|etc.}} up to 10
    anchor names. Put it on the line ABOVE the heading you what it
    anchored to (it looks weird in the same line)

**Image test:**

![](Unsplash_169.jpg "Unsplash_169.jpg")

<references />

[^1]: Ie. whatever the VisualEditor offers, otherwise use Template-codes
    like below for
    color[1](https://www.mediawiki.org/wiki/Template:Color):

        {{color|#229944|Looks good}}