import os
from enum import Enum

from colorama import Fore


class SciCookieErrorType(Enum):
    SH_ERROR_RETURN_CODE = 1
    SH_KEYBOARD_INTERRUPT = 2
    SCICOOKIE_INVALID_PARAMETER = 3
    SCICOOKIE_MISSING_PARAMETER = 4
    SCICOOKIE_INVALID_CONFIGURATION = 5


class SciCookieLogs:
    @staticmethod
    def raise_error(message: str, message_type: SciCookieErrorType):
        print(Fore.RED, f"[EE] {message}", Fore.RESET)
        os._exit(message_type.value)

    @staticmethod
    def info(message: str):
        print(Fore.BLUE, message, Fore.RESET)

    @staticmethod
    def warning(message: str):
        print(Fore.YELLOW, message, Fore.RESET)
