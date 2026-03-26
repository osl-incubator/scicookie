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
                f"The given profile ({profile_name}) is not available.",
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
             
           def _validate_profile(self, profile: dict):
    required_fields = ["name", "version"]

    for field in required_fields:
        if field not in profile:
            raise ValueError(f"Missing required field: '{field}' in profile")

    if not isinstance(profile.get("name"), str):
        raise TypeError("Field 'name' must be a string")

    if "version" in profile and not isinstance(profile["version"], str):
        raise TypeError("Field 'version' must be a string")

        with open(PROFILE_DIR_PATH / f"{self.profile_name}.yaml") as f:
            config_profile = yaml.safe_load(f)
            for name, properties in config_profile.items():
                config[name].update(properties)

                 self._validate_profile(profile_data)

        return config
