"""Profile handles "profiles" defined in the .yaml files."""
from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from scicookie.logs import SciCookieErrorType, SciCookieLogs

PACKAGE_PATH = Path(__file__).parent
PROFILE_DIR_PATH = Path(__file__).absolute().parent / "profiles"


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
        for file in PROFILE_DIR_PATH.glob("*.yaml"):
            self.profiles_available.append(file.stem)

    def read_config(self) -> dict[str, Any]:
        """Read and merge config files safely."""
        with open(PROFILE_DIR_PATH / "base.yaml") as f:
            config = yaml.safe_load(f) or {}

        with open(PROFILE_DIR_PATH / f"{self.profile_name}.yaml") as f:
            config_profile = yaml.safe_load(f) or {}

        self._validate_profile(config_profile)

        for name, properties in config_profile.items():
            if name not in config:
                config[name] = properties
            elif isinstance(config[name], dict) and isinstance(
                properties, dict
            ):
                config[name].update(properties)
            else:
                config[name] = properties

        return config

    def _validate_profile(self, profile: dict[str, Any]) -> None:
        valid_types = {"text", "single-choice", "multiple-choices", "bool"}
        for field_name, field_props in profile.items():
            if not isinstance(field_props, dict):
                continue
            field_type = field_props.get("type")
            if field_type and field_type not in valid_types:
                SciCookieLogs.raise_error(
                    f"Profile field '{field_name}' has invalid type "
                    f"'{field_type}'.",
                    SciCookieErrorType.SCICOOKIE_INVALID_PARAMETER,
                )
