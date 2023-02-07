"""Test get conversion methods."""

import pytest

import usfm_references


@pytest.mark.parametrize(
    "ref,expect",
    [
        ("GEN", "ot"),
        ("NEH", "ot"),
        ("MAT", "nt"),
        ("REV", "nt"),
        ("LKA", "nt"),
        ("PS2", "ap"),
    ],
)
def test_convert_book_to_canon(ref, expect):
    """Test chapter reference validation."""
    assert usfm_references.convert_book_to_canon(ref) == expect


@pytest.mark.parametrize(
    "ref,expect",
    [
        ("Gen 1:1-2", ["Gen 1:1", "Gen 1:2"]),
        ("Psalm 42:9-12", ["Psalm 42:9", "Psalm 42:10", "Psalm 42:11", "Psalm 42:12"]),
        ("MAT", None),
        ("REV.1.1-2", None),
        ("Acts 1:1", None),
    ],
)
def test_convert_verse_range(ref, expect):
    """Test chapter reference validation."""
    assert usfm_references.convert_verse_range(ref) == expect
