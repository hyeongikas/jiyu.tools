import cmd
from sub_menu import SubMenu
from netlimiter_menu import NetLimiterMenu 

class JiyuCLI(cmd.Cmd):
    intro = r"""
     __.__                  __                .__          
    |__|__|___.__.__ __   _/  |_  ____   ____ |  |   ______
    |  |  <   |  |  |  \  \   __\/  _ \ /  _ \|  |  /  ___/
    |  |  |\___  |  |  /   |  | (  <_> |  <_> )  |__\___ \ 
/\__|  |__|/ ____|____/ /\ |__|  \____/ \____/|____/____  >
\______|   \/           \/                              \/  
        .tools
    """
    prompt = "> "

    def do_hello(self, arg):
        """Prints a hello message."""
        print("Hello!")

    def do_1(self, arg):
        """Github & Source Code"""
        print("You selected Github & Source Code.")
        submenu = SubMenu()
        submenu.cmdloop()

    def do_netlimiter(self, arg):
        """Access NetLimiter menu"""
        netlimiter_menu = NetLimiterMenu()
        netlimiter_menu.cmdloop()

    def do_quit(self, arg):
        """Quit the program"""
        print("Exiting Jiyu CLI...")
        return True

if __name__ == '__main__':
    cli = JiyuCLI()
    cli.cmdloop()
