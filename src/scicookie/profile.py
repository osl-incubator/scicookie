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
    config: dict[str, Any]
    profiles_available: list[str]

    def __init__(self, profile_name: str):
        self.config = {}
        self.profiles_available = []
        self._load_profiles_available()

        if profile_name not in self.profiles_available:
            SciCookieLogs.raise_error(
                f"The given profile ({profile_name}) is not available.",
                SciCookieErrorType.SCICOOKIE_INVALID_PARAMETER,
            )

        self.profile_name = profile_name
        self.config = self.read_config()

    def _load_profiles_available(self) -> None:
        """Load available profiles from the profiles directory."""
        self.profiles_available = []
        profiles_path = PROFILE_DIR_PATH

        for file in profiles_path.glob("*.yaml"):
            self.profiles_available.append(file.stem)

    def _validate_profile(self, profile: dict[str, Any]) -> None:
        """Validate the profile schema for required fields and types."""
        required_fields = ["name", "version"]

        for field in required_fields:
            if field not in profile:
                SciCookieLogs.raise_error(
                    f"Profile is missing required field: '{field}'.",
                    SciCookieErrorType.SCICOOKIE_INVALID_PARAMETER,
                )

            if not isinstance(profile[field], str):
                SciCookieLogs.raise_error(
                    f"Profile field '{field}' must be a string.",
                    SciCookieErrorType.SCICOOKIE_INVALID_PARAMETER,
                )

    def read_config(self) -> dict[str, Any]:
        """Read the config file."""
        config: dict[str, Any] = {}

        with open(PROFILE_DIR_PATH / "base.yaml") as f:
            config = yaml.safe_load(f)

        with open(PROFILE_DIR_PATH / f"{self.profile_name}.yaml") as f:
            config_profile = yaml.safe_load(f)

            for name, properties in config_profile.items():
                if name not in config:
                    config[name] = properties
                elif isinstance(config[name], dict) and isinstance(
                    properties, dict
                ):
                    for key, value in properties.items():
                        config[name][key] = value
                else:
                    config[name] = properties

        return config
