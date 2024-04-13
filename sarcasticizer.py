import rumps, pyperclip
class statusarc(rumps.App):
    def __init__(self):
        super(statusarc,self).__init__("sArCaStIcIzEr")
        self.menu = ["sarcasticize clipboard"]
    @rumps.clicked("sarcasticize clipboard")
    def sarcasticize(self,_):
        normal = pyperclip.paste()
        pyperclip.copy(''.join([normal[letter].upper() if letter%2 else normal[letter].lower() for letter in range(0,len(normal))]))
statusarc().run()