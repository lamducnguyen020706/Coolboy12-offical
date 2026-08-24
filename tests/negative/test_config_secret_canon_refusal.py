"""Rejection proofs for the Artifact 021 configuration loader.

Artifact 021's ``Val`` is *"refuses secrets in canon paths"*. A prohibition
asserted without a proof of rejection does not belong in this suite, so the
refusal is exercised here rather than described.

Artifact 015 §15 states the two rules being proved:

    2. No secret may enter ``canon/**``.
    3. No secret may enter ``derived/**``, including caches, indexes,
       projections, coverage, and health reports.

No test here contains real credential material. ``<SECRET>``-style
placeholders are used throughout, in the style Artifact 015 §16 uses.
"""

from __future__ import annotations

import traceback

import pytest

from coolboy12.bootstrap.config import SecretInProtectedPathError, load_config

WORKSPACE = "/workspace"

PLACEHOLDER = "PLACEHOLDER-NOT-A-REAL-SECRET-a1b2c3d4"


@pytest.mark.parametrize(
    "setting",
    [
        "COOLBOY12_API_TOKEN",
        "COOLBOY12_APIKEY_FILE",
        "COOLBOY12_DB_PASSWORD",
        "COOLBOY12_SIGNING_PRIVATE_KEY",
        "COOLBOY12_SERVICE_CREDENTIAL",
        "COOLBOY12_DEPLOY_SECRET",
    ],
)
def test_secret_bearing_setting_in_canon_is_refused(setting):
    """Test C — secret material at a ``canon/**`` location is rejected."""
    with pytest.raises(SecretInProtectedPathError) as raised:
        load_config({setting: "canon/world/access.txt"}, root=WORKSPACE)

    assert raised.value.zone == "canon"


@pytest.mark.parametrize(
    "location",
    [
        "canon/access.txt",
        "canon/world/access.txt",
        "canon/registry/access.txt",
        "./canon/access.txt",
        "docs/../canon/access.txt",
        f"{WORKSPACE}/canon/access.txt",
    ],
)
def test_canon_is_refused_however_the_path_is_written(location):
    """Normalization is part of the refusal, not a way around it."""
    with pytest.raises(SecretInProtectedPathError):
        load_config({"COOLBOY12_API_TOKEN": location}, root=WORKSPACE)


@pytest.mark.parametrize(
    "location",
    [
        "canon/../outside.txt",
        "derived/../outside.txt",
        "nested/../../canon/access.txt",
        "../canon/access.txt",
    ],
)
def test_traversal_out_of_the_workspace_is_not_a_protected_zone(location):
    """Normalization runs in both directions, and it is not a bypass.

    ``canon/../outside.txt`` normalizes to a location that is not in canon, so
    refusing it would be refusing ordinary configuration. The two that climb
    above the workspace land outside it entirely, which Artifact 015 §3 calls
    EXTERNAL — where secret material is supposed to be.

    The reverse direction, ``docs/../canon/...`` normalizing *into* canon, is
    refused; that case is covered above. Neither result depends on any of
    these paths existing.
    """
    config = load_config({"COOLBOY12_API_TOKEN": location}, root=WORKSPACE)

    assert config["API_TOKEN"] == location


@pytest.mark.parametrize(
    "location",
    [
        "derived/indexes/access.txt",
        "derived/caches/access.txt",
        "derived/coverage/access.txt",
        "derived/health/access.txt",
    ],
)
def test_secret_bearing_setting_in_derived_is_refused(location):
    """Artifact 015 §15 rule 3 — generated, cached and diagnostic alike."""
    with pytest.raises(SecretInProtectedPathError) as raised:
        load_config({"COOLBOY12_API_TOKEN": location}, root=WORKSPACE)

    assert raised.value.zone == "derived"


def test_refusal_is_explicit_and_nothing_is_loaded():
    """The refusal is a raised failure, never a silent strip or relocation.

    Artifact 021 must not quietly drop the offending setting and continue with
    the rest of the configuration, because a partly-loaded result would look
    like a success.
    """
    with pytest.raises(SecretInProtectedPathError):
        load_config(
            {
                "COOLBOY12_LOG_LEVEL": "debug",
                "COOLBOY12_API_TOKEN": "canon/world/access.txt",
            },
            root=WORKSPACE,
        )


def test_secret_value_does_not_leak_into_the_failure(caplog, capsys):
    """Test D — the value is absent from the exception, logs and output.

    Artifact 015 §16 keeps credential material out of the boundary entirely.
    The error may name the setting and the zone; it may not carry the value.
    """
    location = f"canon/world/{PLACEHOLDER}.txt"

    with caplog.at_level(0), pytest.raises(SecretInProtectedPathError) as raised:
        load_config(
            {"COOLBOY12_API_TOKEN": location, "COOLBOY12_PASSWORD": PLACEHOLDER},
            root=WORKSPACE,
        )

    error = raised.value
    rendered = "".join(
        traceback.format_exception(type(error), error, error.__traceback__)
    )

    for text in (
        str(error),
        repr(error),
        rendered,
        caplog.text,
        capsys.readouterr().out,
    ):
        assert PLACEHOLDER not in text

    # The safe metadata needed to diagnose it is present.
    assert "COOLBOY12_API_TOKEN" in str(error)
    assert "canon" in str(error)


def test_configuration_repr_does_not_expose_values():
    """A loaded value must not reach a log through the object's repr."""
    config = load_config({"COOLBOY12_API_TOKEN": PLACEHOLDER}, root=WORKSPACE)

    assert PLACEHOLDER not in repr(config)
    assert "API_TOKEN" in repr(config)


def test_secret_held_outside_the_workspace_is_permitted():
    """Artifact 015 §13 permits the loader to consume EXTERNAL secret material.

    The refusal is scoped to canonical zones. A loader that refused every
    secret would have redefined Artifact 015's boundary rather than
    implemented it.
    """
    config = load_config(
        {"COOLBOY12_API_TOKEN": "/etc/coolboy12/access.txt"}, root=WORKSPACE
    )

    assert config["API_TOKEN"] == "/etc/coolboy12/access.txt"


def test_ordinary_configuration_naming_a_canonical_path_is_permitted():
    """Artifact 015 §4 — secret is not all configuration.

    A non-secret setting may legitimately name a canonical location. Refusing
    it would make this module a general write-permission engine, which is
    Artifact 022's responsibility and not Artifact 021's.
    """
    config = load_config({"COOLBOY12_CANON_ROOT": "canon"}, root=WORKSPACE)

    assert config["CANON_ROOT"] == "canon"
