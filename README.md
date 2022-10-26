# USFM-References

[![Build Status](https://travis-ci.org/bbelyeu/usfm-references.svg?branch=main)](https://travis-ci.org/bbelyeu/usfm-references)
[![Coverage Status](https://coveralls.io/repos/github/bbelyeu/usfm-references/badge.svg?branch=main)](https://coveralls.io/github/bbelyeu/usfm-references?branch=main)

A validator & lookup tool for USFM (Unified Standard Format Markers) Biblical references.

## Requirements

This project requires Python 3.6 or higher

## Installation

To install use

    pip install usfm-references

## Usage

Import one of the methods like

    from usfm_references import valid_chapter, valid_chapter_or_intro, valid_usfm, valid_verse, valid_multi_usfm

The validation methods all start with `valid_`. They take a single parameter
which should be a string representation of a USFM reference. And they all
return a boolean value representing whether the string was valid for the
type that the method is validating against.

For example, if you have a string `my_reference` with a reference of Genesis 1:1,
the appropriate USFM reference would be `GEN.1.1`. You could use the valid_verse
method to ensure it is correct like

    if valid_verse(my_reference):
        # do stuff

*NOTE: These validators match a regular expression pattern. That conforms to the
general USFM standard. They do NOT ensure that the USFM actually exists in any
particular Bible version.*

The currently supported validators are:
* `valid_chapter` - Ensures the passed string is a valid USFM chapter reference
* `valid_chapter_or_intro` - Ensures the passed string is either a valid USFM chapter
or intro reference
* `valid_usfm` - Ensures the passed string is a valid USFM reference (can be verse, chapter, or intro)
* `valid_multi_usfm` - Ensures that the passed string is a valid set of USFM reference (can be verse, chapter, or intro)
* `valid_verse` - Ensures the passed string is a valid USFM verse reference

Other methods include conversion such as `convert_book_to_canon`. Import like:

    from usfm_references import convert_book_to_canon

Conversion methods all start with `convert_` and the method names should be self-explanatory
as far as what params go in and what is returned.

`convert_book_to_canon` can be used like:

    canon = convert_book_to_canon("GEN")
    print(canon)  # "ot"

## Development

This project is tested in CI with Python 3.6-3.8.
One of these must be installed before developing and testing locally.

This project uses [pip-tools](https://github.com/jazzband/pip-tools) for dependency management.

### Running tests

``` bash
./linters.sh && pytest --cov=usfm_references tests/
```

### Before committing any code

We have a pre-commit hook which can be used to run linters before committing.
You can symlink it to run before each commit by changing directory to the repo and running

``` bash
cd .git/hooks
ln -s ../../pre-commit pre-commit
```
