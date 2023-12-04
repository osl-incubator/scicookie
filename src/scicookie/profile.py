"""Profile handles "profiles" defined in the .yaml files."""
from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from scicookie.logs import SciCookieErrorType, SciCookieLogs

PACKAGE_PATH = Path(__file__).parent
PROFILE_DIR_PATH = PACKAGE_PATH / "profiles"


class Profile:
    """Profile class that handles profiles defined in the .yaml files."""

    profile_name: str = ""
    config: dict[str, Any] = {}  # noqa: RUF012
    profiles_available: list[str] = []  # noqa: RUF012

    def __init__(self, profile_name: str):
        self._load_profiles_available()

        if profile_name not in self.profiles_available:
            SciCookieLogs.raise_error(
                "The given profiles is not available.",
                SciCookieErrorType.SCICOOKIE_INVALID_PARAMETER,
            )

        self.profile_name = profile_name
        self.config = self.read_config()

    def _load_profiles_available(self):
        self.profiles_available = []

        profiles_path = Path(__file__).absolute().parent / "profiles"

        for file in profiles_path.glob("*.yaml"):
            self.profiles_available.append(file.stem)

    def read_config(self):
        """Read the config file."""
        config = {}
        with open(PROFILE_DIR_PATH / "base.yaml") as f:
            config = yaml.safe_load(f)

        with open(PROFILE_DIR_PATH / f"{self.profile_name}.yaml") as f:
            config_profile = yaml.safe_load(f)
            for name, properties in config_profile.items():
                config[name].update(properties)

        return config
