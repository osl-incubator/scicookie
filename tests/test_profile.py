"""Test the Profile class."""

from __future__ import annotations

from scicookie.profile import PROFILE_DIR_PATH, Profile


def test_read_config_merges_key_not_present_in_base() -> None:
    """A profile key absent from base.yaml must not crash read_config.

    `Profile.read_config` merges each profile's keys into a copy of
    `base.yaml`'s config with `config[name].update(properties)`, which
    raises `KeyError` for any `name` not already present in `base.yaml`
    -- a real risk given profile-related issues (#324, #325, #341) are
    actively adding new profile keys.
    """
    extra_profile_path = PROFILE_DIR_PATH / "__test_extra_key.yaml"
    extra_profile_path.write_text(
        "new_feature_flag:\n  default: true\n  type: bool\n"
    )
    try:
        profile = Profile("__test_extra_key")
        assert profile.config["new_feature_flag"] == {
            "default": True,
            "type": "bool",
        }
    finally:
        extra_profile_path.unlink()
