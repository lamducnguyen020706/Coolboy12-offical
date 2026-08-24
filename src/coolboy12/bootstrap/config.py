"""Configuration loader — Artifact 021.

Artifact 021 · ``src/coolboy12/bootstrap/config.py`` · Own: CONST · RM: n/a ·
T: code · R: IMPL · SoT: DEV-ENV · Auth: none · Canon: n/a · CD: no ·
Ph/St: P0/0e · Req: BR-06 · BP: §9.5 · RMS: n/a · H: 005,015 · S: — · LS: — ·
G: — · → 022 · Val: refuses secrets in canon paths · Done: loads ·
Why: config must not leak · Risk: low · ∥: yes

What this module is
-------------------
An execution-environment facility::

    execution environment configuration
            ↓
        this loader
            ↓
      runtime configuration

Blueprint §9.5 places the execution environment *above* coolboy12 and
*outside* it — "the workshop, not the building" — and draws four prohibitions
from that, the third being that the environment owns no semantics. This module
is environment machinery. ``Auth: none``. Nothing it returns is Canon, a
Record, a Registry definition, or a semantic of any Record Model, and no value
loaded here acquires authority by having been loaded (P-31, P-33, I-84).

What this module is not
-----------------------
Not a Canon manager, Registry loader, Record Model loader, mutation mechanism,
canonical writer, derived-store manager, rebuild engine, staleness engine,
validation framework, secret-management platform, permission framework, policy
engine, or configuration database. It writes nothing, anywhere: every function
below is a pure function of its arguments and touches no filesystem path, so it
cannot modify ``canon/**``, ``derived/**``, or any other state.

Adjacent artifacts, and where this one stops
--------------------------------------------
* **015** ``docs/boundaries/secrets.md`` — the constitutional secrets and
  configuration boundary. It is the source for everything below; this module
  implements the loader inside it and redefines none of it.
* **017** ``docs/boundaries/canonical_zones.md`` — owns the canonical zone
  declaration. This module is *not* that declaration and does not reproduce
  its taxonomy. It recognizes exactly the two directory names Artifact 015
  §15 rules 2 and 3 name — ``canon/`` and ``derived/`` — because its own
  ``Val`` requires it to, and nothing more.
* **020** ``docs/conventions/rebuild.md`` — a convention, not a runtime
  dependency. Nothing here imports or calls rebuild machinery.
* **022** ``.claude/hooks/canon_deny.py`` — enforces direct-write denial for
  canonical paths. **That is not this module's job.** This module refuses a
  configuration; it does not intercept, deny, or police filesystem writes.
* **023** ``.claude/hooks/zones.json`` — machine-readable zone permissions,
  and a later artifact. Not imported, not required, not anticipated here.

Artifact 021's declared hard dependencies are ``005,015``. It imports nothing
outside the Python standard library and nothing from a later artifact.
"""

from __future__ import annotations

import os
from collections.abc import Iterator, Mapping
from types import MappingProxyType

__all__ = [
    "Config",
    "ConfigError",
    "MalformedConfigError",
    "SecretInCanonicalPathError",
    "load_config",
]


ENV_PREFIX = "COOLBOY12_"
"""Namespace this loader reads from the environment.

No authoritative source names a configuration source, a file format, or a
variable namespace. Artifact 015 §13 states this explicitly: the exact secret
source "environment variable, file, external provider" is "not fixed here,
because the source does not fix them" and is Artifact 021's implementation
choice. Environment variables are the smallest environment-native mechanism
available — Blueprint §26.8 already lists runtime and command execution among
what the environment provides — and they need no new file, no new format, and
no dependency beyond the standard library.
"""


_CANONICAL_ZONE_DIRECTORIES = ("canon", "derived")
"""The two directory names a secret may never reach.

Artifact 015 §15 states them as rules 2 and 3: "No secret may enter
``canon/**``" and "No secret may enter ``derived/**``". Artifact 021's own
``Val`` is "refuses secrets in canon paths".

This tuple is a *recognition* of those two names, not a zone declaration.
Artifact 017 declares the canonical zones and Artifact 023 will supply them
machine-readably; neither is duplicated, extended, or pre-empted here.
"""


_SECRET_NAME_MARKERS = (
    "secret",
    "credential",
    "token",
    "api_key",
    "apikey",
    "private_key",
    "password",
)
"""Substrings that mark a setting name as secret-bearing.

Taken from Artifact 015 §4, which — absent a source-defined taxonomy — uses
"the ordinary sense of the term": "credentials, tokens, API keys, private
keys, passwords, and connection material carrying such data". §4 states that
this list is "descriptive, not an authoritative COOLBOY12 taxonomy", and it is
not one here either. No Registry ``CONTROLLED-VOCABULARY`` for secret classes
exists, and this module creates none.

Matching is a case-insensitive substring test, so it over-matches rather than
under-matches. A setting merely *named* like a secret is refused when it points
into a canonical zone even if its value holds nothing sensitive. That direction
is deliberate: the cost of a false refusal is a rename, and the cost of a false
acceptance is the boundary Artifact 015 exists to hold.
"""


class ConfigError(Exception):
    """Base class for every failure this loader raises.

    A configuration failure stays a failure. This module has no fallback that
    converts an invalid configuration into an empty one, and no ``except``
    clause that swallows an error and returns a default.
    """


class MalformedConfigError(ConfigError):
    """The environment holds a ``COOLBOY12_`` entry that is not a setting."""


class SecretInCanonicalPathError(ConfigError):
    """A secret-bearing setting designates a location inside a canonical zone.

    This is Artifact 021's ``Val`` — "refuses secrets in canon paths" — as a
    raised exception.

    The exception carries the setting *name* and the *zone*, and never the
    value. Artifact 015 §16 keeps real credential material out of the boundary
    entirely; the same rule applies to anything this module emits. There is no
    attribute, message, argument, or representation on this class through which
    a configured value can reach a log, a console, or a traceback.
    """

    def __init__(self, setting: str, zone: str) -> None:
        self.setting = setting
        self.zone = zone
        super().__init__(
            f"{setting}: secret-bearing configuration designates a location "
            f"inside the {zone}/ zone. Secrets are EXTERNAL and may never "
            f"enter canon/** or derived/** (Artifact 015 §15, rules 2-3). "
            f"The value is withheld from this message."
        )


class Config:
    """An immutable, read-only view of the loaded environment configuration.

    Holds environment information and nothing else. There is deliberately no
    field for Canon, Registry meaning, Record Model semantics, world truth,
    epistemic state, production state, visual semantics, issue semantics, or
    Human Gate behaviour: configuration is not domain truth, and a field here
    would be exactly the "API through which configuration decides what the
    world's truth is" that Blueprint §9.5's third prohibition rules out.

    Settings are exposed with the ``COOLBOY12_`` prefix stripped. The mapping
    is read-only and the instance carries no mutable state, so a caller cannot
    reach back through it and change what another caller sees.
    """

    __slots__ = ("_settings",)

    def __init__(self, settings: Mapping[str, str]) -> None:
        self._settings = MappingProxyType(dict(settings))

    @property
    def settings(self) -> Mapping[str, str]:
        """The accepted settings, read-only."""
        return self._settings

    def get(self, name: str, default: str | None = None) -> str | None:
        """Return the setting ``name``, or ``default`` when it is absent."""
        return self._settings.get(name, default)

    def __getitem__(self, name: str) -> str:
        return self._settings[name]

    def __contains__(self, name: object) -> bool:
        return name in self._settings

    def __iter__(self) -> Iterator[str]:
        return iter(self._settings)

    def __len__(self) -> int:
        return len(self._settings)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Config):
            return NotImplemented
        return dict(self._settings) == dict(other._settings)

    def __hash__(self) -> int:
        return hash(frozenset(self._settings.items()))

    def __repr__(self) -> str:
        """Name the settings; never show a value.

        The default representation of a container would print every loaded
        value, which is how a credential reaches a log or a traceback frame.
        Artifact 015 forbids that outcome, so the values are not in the
        representation at all — for any setting, secret-named or not, because
        the loader cannot tell which ordinary-looking name holds sensitive
        material and guessing is not a boundary.
        """
        names = ", ".join(sorted(self._settings))
        return f"Config(settings=[{names}])"


def load_config(
    environ: Mapping[str, str] | None = None,
    *,
    root: str | os.PathLike[str] | None = None,
) -> Config:
    """Load the execution environment's configuration, or refuse it.

    :param environ: the environment mapping to read. Defaults to
        ``os.environ``. It is a parameter so that the loader is a pure
        function of its inputs: the same mapping and the same ``root`` always
        produce the same result, with no wall clock, no randomness, no
        network, no Git history, no previous derived state, and no cache
        involved (the hidden dependencies Artifact 020 §7 prohibits).
    :param root: the workspace directory that relative configured paths are
        resolved against, for the canonical-zone check only. Defaults to the
        current working directory — the workspace the execution environment
        provides (Blueprint §26.8). It is never read from, written to, or
        required to exist; the check below is purely lexical.

    :returns: a :class:`Config` holding the accepted settings, with the
        ``COOLBOY12_`` prefix stripped from each name.

    :raises MalformedConfigError: an entry in the namespace is not a setting.
    :raises SecretInCanonicalPathError: a secret-bearing setting designates a
        location inside ``canon/`` or ``derived/``.

    No setting is required. No authoritative source names one, and inventing a
    mandatory key here would be invented architecture rather than a loaded
    configuration — so an environment with no ``COOLBOY12_`` entries at all
    loads successfully and yields an empty :class:`Config`.
    """
    source = os.environ if environ is None else environ
    base = os.getcwd() if root is None else os.fspath(root)

    accepted: dict[str, str] = {}
    for key in sorted(source):
        if not key.startswith(ENV_PREFIX):
            continue

        name = key[len(ENV_PREFIX) :]
        if not name:
            raise MalformedConfigError(
                f"{ENV_PREFIX!r} is present with an empty setting name. The "
                f"namespace requires {ENV_PREFIX}<NAME>."
            )

        value = source[key]
        if _names_secret_material(name):
            zone = _canonical_zone_designated_by(value, base)
            if zone is not None:
                raise SecretInCanonicalPathError(setting=key, zone=zone)

        accepted[name] = value

    return Config(accepted)


def _names_secret_material(name: str) -> bool:
    """Whether ``name`` marks its setting as secret-bearing (Artifact 015 §4)."""
    lowered = name.lower()
    return any(marker in lowered for marker in _SECRET_NAME_MARKERS)


def _canonical_zone_designated_by(value: str, base: str) -> str | None:
    """Return the canonical zone ``value`` points into, or ``None``.

    Purely lexical. The path is normalized and compared against ``base``; the
    filesystem is never consulted, nothing is opened, and nothing is created.
    That is what makes it safe for a loader to run this check at all: it can
    neither read a canonical record nor bring one into existence.

    A location outside ``base`` is not in a canonical zone. Secret material
    held outside the workspace is exactly where Artifact 015 §3 says it
    belongs — EXTERNAL — and Artifact 015 §13 permits the loader to consume it
    for runtime use.
    """
    candidate = value.strip()
    if not candidate:
        return None

    resolved = os.path.normpath(os.path.join(base, candidate))
    try:
        relative = os.path.relpath(resolved, base)
    except ValueError:
        # A different drive on Windows: outside the workspace, so not a zone.
        return None

    if relative == os.curdir or relative.startswith(os.pardir):
        return None

    head = relative.replace("\\", "/").split("/", 1)[0]
    return head if head in _CANONICAL_ZONE_DIRECTORIES else None
