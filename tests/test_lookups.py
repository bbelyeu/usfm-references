"""Test lookup USFM functions."""

import pytest

import usfm_references

def test_book_name_lookup():
    """This function tests the book name lookup functionality."""
    book_usfm = usfm_references.book_lookup("Matt")
    assert book_usfm == "MAT"

@pytest.mark.parametrize(
    "query,expect",
    [(i, i) for i in usfm_references.BOOKS] + [("ZZZ", None), ("zzz", None)],
)
def test_book_lookup_by_usfm(query, expect):
    """This tests asserts books usfms can be looked up by their USFM"""
    assert usfm_references.book_lookup(query) == expect