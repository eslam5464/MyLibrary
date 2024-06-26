import functools
from typing import Any, Callable

from lib.utils.apps import ffmpeg, libre_office


def check_libre_office(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator that ensures LibreOffice is installed before executing the decorated function.
    If LibreOffice is not installed, the decorator will install it automatically before proceeding
    with the execution of the function.
    :param func: The function to be decorated.
    :return: A wrapped function that ensures LibreOffice is installed before execution.
    """

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        if not libre_office.check_libre_office_installed():
            print("LibreOffice is not installed. Installing...")
            libre_office.install_libre_office()

        value = func(*args, **kwargs)

        return value

    return wrapper


def check_ffmpeg(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator that ensures ffmpeg is installed before executing the decorated function.
    If ffmpeg is not installed, the decorator will install it automatically before proceeding
    with the execution of the function.

    :param func: The function to be decorated.
    :return: A wrapped function that ensures ffmpeg is installed before execution.
    """

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        if not ffmpeg.check_ffmpeg_installed():
            print("ffmpeg is not installed. Installing...")
            ffmpeg.install_ffmpeg()

        value = func(*args, **kwargs)

        return value

    return wrapper
