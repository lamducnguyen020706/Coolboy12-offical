"""Unit tests for the Artifact 021 configuration loader.

Proves the single responsibility Artifact 021 declares: ``Done: loads``.
Rejection proofs live in ``tests/negative/`` and boundary proofs in
``tests/boundary/``, per the suite responsibilities Artifact 010 established.

No test here contains real credential material. Every secret-shaped value is a
placeholder, in the style Artifact 015 §16 uses.
"""

from __future__ import annotations

import traceback

import pytest

from coolboy12.bootstrap.config import (
    ENV_PREFIX,
    Config,
    MalformedConfigError,
    load_config,
)


def test_valid_configuration_loads(tmp_path):
    """Test A — a valid environment configuration loads.

    The whole of ``Done: loads``: the right type, the right settings, the
    right values, and nothing else carried along.
    """
    config = load_config(
        {
            "COOLBOY12_LOG_LEVEL": "debug",
            "COOLBOY12_WORKSPACE": "src",
            "PATH": "/usr/bin",
        },
        root=tmp_path,
    )

    assert isinstance(config, Config)
    assert config.get("LOG_LEVEL") == "debug"
    assert config["WORKSPACE"] == "src"

    # The representation is exactly the two namespaced settings, as strings.
    assert dict(config.settings) == {"LOG_LEVEL": "debug", "WORKSPACE": "src"}
    assert len(config) == 2
    assert all(isinstance(value, str) for value in config.settings.values())


def test_coolboy12_namespace_is_stripped():
    """``COOLBOY12_FOO`` is loaded as ``FOO``.

    The prefix selects the namespace; it is not part of the setting's name.
    """
    config = load_config({"COOLBOY12_FOO": "bar"}, root="/workspace")

    assert config["FOO"] == "bar"
    assert "COOLBOY12_FOO" not in config
    assert list(config) == ["FOO"]


def test_unrelated_environment_variables_are_ignored():
    """Namespace isolation — an ordinary environment is not configuration."""
    config = load_config(
        {
            "PATH": "/usr/bin",
            "HOME": "/root",
            "SHELL": "/bin/sh",
            "UNRELATED_VAR": "x",
            "COOLBOY12_LOG_LEVEL": "debug",
        },
        root="/workspace",
    )

    assert dict(config.settings) == {"LOG_LEVEL": "debug"}


def test_prefix_must_match_exactly():
    """A name that merely resembles the namespace is not in it."""
    config = load_config(
        {"COOLBOY12": "x", "COOLBOY123_A": "y", "XCOOLBOY12_B": "z"},
        root="/workspace",
    )

    assert len(config) == 0


def test_iteration_order_is_deterministic():
    """The public iteration order is sorted, not insertion- or hash-dependent."""
    config = load_config(
        {"COOLBOY12_C": "3", "COOLBOY12_A": "1", "COOLBOY12_B": "2"},
        root="/workspace",
    )

    assert list(config) == ["A", "B", "C"]


def test_empty_environment_loads_successfully(tmp_path):
    """No setting is required, because no authoritative source names one.

    The result is a valid, empty configuration — not a failure, and not None.
    """
    config = load_config({}, root=tmp_path)

    assert isinstance(config, Config)
    assert len(config) == 0
    assert dict(config.settings) == {}


def test_malformed_namespace_entry_fails_explicitly():
    """Test B — a malformed entry fails, and does not degrade to a default.

    The one structural rule of the namespace is that a setting has a name.
    An invalid configuration stays invalid; it never becomes an empty one.
    """
    orphaned_value = "ORPHANED-PLACEHOLDER-NOT-A-REAL-SECRET-e5f6a7b8"

    with pytest.raises(MalformedConfigError) as raised:
        load_config({ENV_PREFIX: orphaned_value}, root="/workspace")

    # An entry with no name may still hold sensitive material, so the value is
    # withheld here for the same reason it is withheld from a zone refusal.
    error = raised.value
    rendered = "".join(
        traceback.format_exception(type(error), error, error.__traceback__)
    )
    for text in (str(error), repr(error), rendered):
        assert orphaned_value not in text


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
