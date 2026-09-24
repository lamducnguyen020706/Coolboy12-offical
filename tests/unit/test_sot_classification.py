"""Unit proofs for the Artifact 050 source-of-truth classification mechanism.

Row 050's ``Val``: *"every record carries exactly one class"*. These tests
prove the positive half — each of Blueprint §29.6a's five classes is accepted
and named — for records of every Record Model alike. Nothing here is a Record
and nothing here is canonical.
"""

from __future__ import annotations

import pytest

from coolboy12.kernel.sot import (
    SOT_CLASS_FIELD,
    SourceOfTruthClass,
    SourceOfTruthError,
    SourceOfTruthErrorCode,
    validate_record_source_of_truth,
    validate_source_of_truth_class,
)

FIVE = ("AUTHORITATIVE", "DERIVED", "CACHED", "TEMPORARY", "EXTERNAL")


def test_the_vocabulary_is_exactly_the_five_of_29_6a():
    """Closed and exact: five members, spelled as §29.6a spells them."""
    assert tuple(member.value for member in SourceOfTruthClass) == FIVE
    assert tuple(SourceOfTruthClass.__members__) == FIVE


@pytest.mark.parametrize("value", FIVE)
def test_each_class_is_accepted_and_named(value):
    assert validate_source_of_truth_class(value) is SourceOfTruthClass[value]


@pytest.mark.parametrize("member", list(SourceOfTruthClass))
def test_a_member_is_accepted_as_itself(member):
    assert validate_source_of_truth_class(member) is member


def test_the_envelope_field_is_spelled_as_033_spells_it():
    assert SOT_CLASS_FIELD == "sot_class"


@pytest.mark.parametrize("value", FIVE)
def test_a_record_carrying_one_class_is_accepted(value):
    record = {"sot_class": value}

    assert validate_record_source_of_truth(record) is SourceOfTruthClass[value]


@pytest.mark.parametrize("partition", ["W", "E", "P", "R", "V", "I"])
def test_the_same_mechanism_serves_all_six_record_models(partition):
    """RM: all — one mechanism, the same answer, whichever model owns the Record.

    The partition is present in the record and is not read.
    """
    record = {"partition": partition, "sot_class": "AUTHORITATIVE"}

    assert validate_record_source_of_truth(record) is SourceOfTruthClass.AUTHORITATIVE


def test_a_refusal_carries_its_code():
    """The code is the contract; the message is not."""
    with pytest.raises(SourceOfTruthError) as excinfo:
        validate_source_of_truth_class("DEV-ENV")

    assert excinfo.value.code is SourceOfTruthErrorCode.INVALID_SOURCE_OF_TRUTH_CLASS
    assert isinstance(excinfo.value, ValueError)
