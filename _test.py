# test_jiyu_cli

import pytest
from jiyu_cli import JiyuCLI

@pytest.fixture
def cli():
    return JiyuCLI()

def test_hello(cli, capsys):
    cli.do_hello("")
    captured = capsys.readouterr()
    assert "Hello!" in captured.out

def test_menu_navigation(cli, capsys):
    # Test navigation to GitHub menu
    cli.do_1("")
    captured = capsys.readouterr()
    assert "You selected Github & Source Code" in captured.out
    assert "(Github Menu)" in captured.out

    # Test navigation back to main menu
    cli.do_back("")
    captured = capsys.readouterr()
    assert "(Main Menu)" in captured.out

def test_netlimiter_menu(cli, capsys):
    # Test navigation to NetLimiter menu
    cli.do_netlimiter("")
    captured = capsys.readouterr()
    assert "(NetLimiter Menu)" in captured.out

    # Test install option
    cli.do_install("")
    captured = capsys.readouterr()
    assert "Installing NetLimiter" in captured.out

    # Test patch option
    cli.do_patch("")
    captured = capsys.readouterr()
    assert "Patching NetLimiter" in captured.out

    # Test exit option
    cli.do_exit("")
    captured = capsys.readouterr()
    assert "Exiting NetLimiter menu" in captured.out
