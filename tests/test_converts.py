"""Test get conversion methods."""

import pytest

from usfm_references import convert_book_to_canon


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
    assert convert_book_to_canon(ref) == expect
