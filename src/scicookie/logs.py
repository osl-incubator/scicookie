"""Module for functions and classes for systen logs."""
import os

from enum import Enum

from colorama import Fore


class SciCookieErrorType(Enum):
    """Enum class for the error codes."""

    SH_ERROR_RETURN_CODE = 1
    SH_KEYBOARD_INTERRUPT = 2
    SCICOOKIE_INVALID_PARAMETER = 3
    SCICOOKIE_MISSING_PARAMETER = 4
    SCICOOKIE_INVALID_CONFIGURATION = 5


class SciCookieLogs:
    """Main log for print and raise messages to the system."""

    @staticmethod
    def raise_error(message: str, message_type: SciCookieErrorType):
        """Print an error message and exit with the given error code."""
        print(Fore.RED, f"[EE] {message}", Fore.RESET)
        os._exit(message_type.value)

    @staticmethod
    def info(message: str):
        """Print an info message."""
        print(Fore.BLUE, message, Fore.RESET)

    @staticmethod
    def warning(message: str):
        """Print a warning message."""
        print(Fore.YELLOW, message, Fore.RESET)
