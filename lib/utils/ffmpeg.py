import subprocess
import sys

from lib.utils.operating_systems.mac import is_homebrew_installed, install_homebrew
from lib.utils.operating_systems.windows import install_chocolatey, is_chocolatey_installed


def install_ffmpeg():
    """
    Installs ffmpeg on the system based on the operating system.
    :raises OSError: If the platform is unsupported.
    """
    check = True

    if sys.platform == 'win32':
        if not is_chocolatey_installed():
            print("Chocolatey is not installed. Installing Chocolatey...")
            install_chocolatey()
        subprocess.run(['choco', 'install', 'ffmpeg-full', '-y'], check=check)
    elif sys.platform == 'darwin':
        if not is_homebrew_installed():
            print("Homebrew is not installed. Installing Homebrew...")
            install_homebrew()
        subprocess.run(['brew', 'install', 'ffmpeg'], check=check)
    elif sys.platform == 'linux':
        subprocess.run(['sudo', 'apt-get', 'update'], check=check)
        subprocess.run(['sudo', 'apt-get', 'install', '-y', 'ffmpeg'], check=check)
    else:
        raise OSError('Unsupported platform')


def check_ffmpeg_installed():
    """
    Checks if ffmpeg is installed on the system.
    :return: True if ffmpeg is installed, False otherwise.
    """
    try:
        subprocess.run(['ffmpeg', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False