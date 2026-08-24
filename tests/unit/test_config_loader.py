"""Unit tests for the Artifact 021 configuration loader.

Proves the single responsibility Artifact 021 declares: ``Done: loads``.
Rejection proofs live in ``tests/negative/`` and boundary proofs in
``tests/boundary/``, per the suite responsibilities Artifact 010 established.

No test here contains real credential material. Every secret-shaped value is a
placeholder, in the style Artifact 015 §16 uses.
"""

from __future__ import annotations

import pytest

from coolboy12.bootstrap.config import (
    ENV_PREFIX,
    Config,
    MalformedConfigError,
    load_config,
)


def test_valid_configuration_loads():
    """Test A — a valid environment configuration loads."""
    config = load_config(
        {
            "COOLBOY12_LOG_LEVEL": "debug",
            "COOLBOY12_WORKSPACE": "src",
            "PATH": "/usr/bin",
        },
        root="/workspace",
    )

    assert config.get("LOG_LEVEL") == "debug"
    assert config["WORKSPACE"] == "src"


def test_only_the_namespace_is_read():
    """Entries outside ``COOLBOY12_`` are not configuration and are ignored."""
    config = load_config({"PATH": "/usr/bin", "HOME": "/root"}, root="/workspace")

    assert len(config) == 0
    assert "PATH" not in config


def test_empty_environment_loads_successfully():
    """No setting is required, because no authoritative source names one."""
    assert len(load_config({}, root="/workspace")) == 0


def test_malformed_namespace_entry_fails_explicitly():
    """Test B — a malformed entry fails, and does not degrade to a default.

    The one structural rule of the namespace is that a setting has a name.
    An invalid configuration stays invalid; it never becomes an empty one.
    """
    with pytest.raises(MalformedConfigError):
        load_config({ENV_PREFIX: "orphaned"}, root="/workspace")


def test_loading_is_deterministic():
    """The same inputs produce the same result — no hidden state."""
    environ = {"COOLBOY12_A": "1", "COOLBOY12_B": "2"}

    assert load_config(environ, root="/workspace") == load_config(
        environ, root="/workspace"
    )


def test_returned_configuration_is_read_only():
    """A caller cannot mutate the loaded configuration through the result."""
    config = load_config({"COOLBOY12_A": "1"}, root="/workspace")

    with pytest.raises(TypeError):
        config.settings["A"] = "2"  # type: ignore[index]

    assert config["A"] == "1"


def test_settings_are_isolated_from_the_source_mapping():
    """Mutating the source environment afterwards does not change the result."""
    environ = {"COOLBOY12_A": "1"}
    config = load_config(environ, root="/workspace")

    environ["COOLBOY12_A"] = "mutated"

    assert config["A"] == "1"


def test_configuration_carries_no_domain_semantics():
    """Configuration is environment information, never domain truth.

    Blueprint §9.5's third prohibition: the environment owns no semantics.
    A field for any of these would be the API through which configuration
    decides what the world's truth is.
    """
    forbidden = (
        "world_truth",
        "canon_truth",
        "canon",
        "registry",
        "registry_semantics",
        "record_model",
        "character_state",
        "issue_semantics",
        "simulation_truth",
        "epistemic_state",
        "human_gate",
    )

    surface = {attribute.lower() for attribute in dir(Config)}
    assert surface.isdisjoint(forbidden)
