# sarcasticizer
a qUiCk aNd uSeFuL MaCoS StAtUsBaR UtIlItY To aPpLy [aLtErNaTiNg cApItAlS](https://en.wikipedia.org/wiki/Alternating_caps) To cOpIeD TeXt! 

unzip and download the portable file from [Releases](https://github.com/AashvikTyagi/sarcasticizer/releases/)!

sticky caps are generally used to show mockery while quoting someone. Sarcasticizer is an application that runs only in the macos statusbar and applies the effect on your copied text!

it was made in python using rumpus and py2app for the app management and pyperclip for clipboard operations.
source code is right above in the files and i'd recommend recompiling the setup.py using py2app as you can learn online because i'd never used it before and have no idea why the application ended up being 28mb (!!!!!!!!!!!!!!!!!!).

sarcasticizer does NOT steal your data. compile it for yourself if you so care about your privacy.






honestly incredibly useful for online debates!


for a string `normal`, `''.join([normal[letter].upper() if letter%2 else normal[letter].lower() for letter in range(0,len(normal))])`
