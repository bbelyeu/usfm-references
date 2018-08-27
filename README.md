# USFM-References

[![Build Status](https://travis-ci.org/bbelyeu/usfm-references.svg?branch=master)](https://travis-ci.org/bbelyeu/usfm-references)
[![Coverage Status](https://coveralls.io/repos/github/bbelyeu/usfm-references/badge.svg?branch=master)](https://coveralls.io/github/bbelyeu/usfm-references?branch=master)

A validator for USFM (Unified Standard Format Markers) Biblical references

## Requirements

This project requires Python 3.5 or higher

## Installation

To install use

    pip install usfm-references

## Usage

Import one of the methods like

    from usfm_references import valid_chapter, valid_chapter_or_intro, valid_usfm, valid_verse

The validation methods all start with `valid_`. They take a single parameter
which should be a string representation of a USMF reference. And they all
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
* `valid_verse` - Ensures the passed string is a valid USFM verse reference

## Development

This project was written with Python 3.6 and is tested in CI with Python 3.5-3.6.
One of these must be installed before developing and testing locally.

On a mac you can use the following commands to get up and running.
``` bash
brew install python3.6
```
otherwise run
``` bash
brew upgrade python3.6
```
to make sure you have an up to date version.

This project uses [pipenv](https://docs.pipenv.org) for dependency management. Install pipenv
``` bash
pip3 install pipenv
```

setup the project env
``` base
pipenv install --three --dev
```

create a .env file using this sample
``` bash
export PYTHONPATH=`pwd`
```

now load virtualenv and any .env file
```bash
pipenv shell
```

### Running tests

``` bash
./linters.sh && pytest --cov=usfm_references tests/
```

### Before committing any code

We have a pre-commit hook which should be setup.
You can symlink it to run before each commit by changing directory to the repo and running

``` bash
cd .git/hooks
ln -s ../../pre-commit pre-commit
```
