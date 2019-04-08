"""wslpy.winexec

This is the execution class to execute commands from dirfferent windows executables
"""
import subprocess

def CmdExec(command):
    """
    Execute cmd command.

    Parameters
    ----------
    command : str
        string of cmd.exe commands.
    """
    cmd = u"cmd.exe /c \""+command+u"\""
    subprocess.call(cmd, shell=True)


def PwShExec(command):
    """
    Execute PowerShell(5.*) command.

    Parameter
    ---------
    command : str
        string of powershell.exe command.
    """
    cmd = u"powershell.exe -NoProfile -NonInteractive -Command \""+command+u"\""
    subprocess.call(cmd, shell=True)


def PwShCrExec(command):
    """
    Execute PowerShell Core 6 command.

    Parameter
    ---------
    command : str
        string of pwsh.exe command.
    """
    cmd = u"pwsh.exe -NoProfile -NonInteractive -Command \""+command+u"\""
    subprocess.call(cmd, shell=True)