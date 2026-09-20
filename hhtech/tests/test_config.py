"""HHTECH config/credential loading. No network, no real key required."""

from __future__ import annotations

import pytest
from audit_runner import config
from audit_runner.errors import InputError


def test_load_config_missing_key(monkeypatch):
    monkeypatch.delenv(config.API_KEY_ENV_VAR, raising=False)
    with pytest.raises(InputError):
        config.load_config()


def test_load_config_blank_key(monkeypatch):
    monkeypatch.setenv(config.API_KEY_ENV_VAR, "   ")
    with pytest.raises(InputError):
        config.load_config()


def test_load_config_ok(monkeypatch):
    monkeypatch.setenv(config.API_KEY_ENV_VAR, "fixture-key")
    cfg = config.load_config()
    assert cfg.api_key == "fixture-key"
    assert cfg.endpoint == "https://hhtechapi.net/v1/chat/completions"
    # The model is operator-owned and has been changed deliberately twice
    # (gpt-5.6-luna -> gpt-5.6-sol -> gpt-6-astra). Pinning the literal here
    # turned every intentional change into a red suite while proving nothing
    # about load_config, which is what this test exists to check. Assert the
    # plumbing instead: the config surfaces the module's declared model, and
    # that model is a real non-empty value.
    assert cfg.model == config.HHTECH_MODEL
    assert isinstance(cfg.model, str) and cfg.model.strip()


def test_config_never_touches_anthropic_env(monkeypatch):
    monkeypatch.delenv("ANTHROPIC_BASE_URL", raising=False)
    monkeypatch.delenv("ANTHROPIC_AUTH_TOKEN", raising=False)
    monkeypatch.setenv(config.API_KEY_ENV_VAR, "fixture-key")
    config.load_config()
    import os

    assert "ANTHROPIC_BASE_URL" not in os.environ
    assert "ANTHROPIC_AUTH_TOKEN" not in os.environ
