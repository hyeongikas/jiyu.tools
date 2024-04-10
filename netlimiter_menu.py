import cmd
import os
import requests
from dankware import cls, clr, align, rm_line, red, red_dim

class NetLimiterMenu(cmd.Cmd):
    prompt = "(NetLimiter Menu) > "

    def do_install(self, arg):
        """Install NetLimiter"""
        print("Installing NetLimiter...")
        self._install_netlimiter()

    def do_patch(self, arg):
        """Patch NetLimiter"""
        print("Patching NetLimiter...")
        self._patch_netlimiter()

    def do_exit(self, arg):
        """Exit NetLimiter menu"""
        print("Exiting NetLimiter menu...")
        return True

    def _install_netlimiter(self):
        # Function to install NetLimiter
        session = requests.Session()
        headers = {"User-Agent": f"jiyu.tool {os.environ['JIYU_TOOL_VERSION']}"}

        # Check if NetLimiter is already installed
        if os.path.isfile(r"C:\Program Files\Locktime Software\NetLimiter\NetLimiter.dll"):
            print(clr(f"\n  - NetLimiter found!"))
        else:
            print(clr(f"\n  - NetLimiter not found!\n\n  - Downloading NetLimiter..."))
            url = 'https://download.netlimiter.com' + session.get("https://www.netlimiter.com/download").content.decode().split('https://download.netlimiter.com',1)[1].split('"',1)[0]
            data = session.get(url, headers=headers).content
            with open('netlimiter.exe', 'wb') as file:
                file.write(data)

            os.system('netlimiter.exe')
            input(clr(f"\n  > Press [ ENTER ] after installing NetLimiter... "))

    def _patch_netlimiter(self):
        # Function to patch NetLimiter
        session = requests.Session()
        headers = {"User-Agent": f"jiyu.tool {os.environ['JIYU_TOOL_VERSION']}"}

        sha = session.get("https://api.github.com/repos/Baseult/NetLimiterCrack/commits?path=NetLimiter%20Crack.exe&page=1&per_page=1", headers=headers).json()[0]['sha']

        def get_patcher():
            data = session.get("https://github.com/Baseult/NetLimiterCrack/raw/main/NetLimiter%20Crack.exe", headers=headers).content
            print(clr(f"\n  - NetLimiter-Patcher downloaded successfully!"))
            while True:
                try:
                    with open('netlimiter-patcher.exe', 'wb') as file:
                        file.write(data)
                    print(clr(f"\n  - NetLimiter-Patcher saved successfully!"))
                    break
                except Exception as exc:
                    input(clr(f"\n  > Failed to save NetLimiter-Patcher! {exc} | Press [ ENTER ] to try again... ",2))
                    rm_line(); rm_line()

        if os.path.isfile('netlimiter-patcher.exe'):
            with open('sha.txt', 'r', encoding='utf-8') as file:
                _sha = file.read()
            if _sha == sha:
                print(clr(f"\n  - NetLimiter-Patcher is up-to-date!"))
            else:
                print(clr(f"\n  - Updating NetLimiter-Patcher..."))
                get_patcher()
                with open('sha.txt', 'w', encoding='utf-8') as file:
                    file.write(sha)
        else:
            print(clr(f"\n  - Downloading NetLimiter-Patcher..."))
            get_patcher()

        input(clr(f"\n  > Hit [ ENTER ] to start NetLimiter-Patcher... "))
        cls(); print(clr(f"\n  - Close the patcher to return to the menu..."))
        os.system('netlimiter-patcher.exe')
