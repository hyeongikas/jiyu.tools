import cmd

class SubMenu(cmd.Cmd):
    prompt = "(Github Menu) > "

    def do_github(self, arg):
        """Go to github.com/hyeongikas"""
        print("Opening github.com/hyeongikas")

    def do_source(self, arg):
        """View the source code: github.com/hyeongikas/jiyutools"""
        print("Opening github.com/hyeongikas/jiyutools")

    def do_back(self, arg):
        """Go back to the main menu"""
        return True

    def precmd(self, line):
        if line.strip() == "":
            return "back"
        return line
