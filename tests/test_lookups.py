"""Test lookup USFM functions."""

import pytest

import usfm_references

def test_book_name_lookup():
    """This function tests the book name lookup functionality."""
    book_usfm = usfm_references.book_lookup("Matt")
    assert book_usfm == "MAT"