#!/bin/bash

echo "> running black..."
black . --check
if [ $? != 0 ]; then
    exit 1
else
    echo "black code format looks good!"
fi
echo

echo "> running isort..."
isort . --check --diff --settings-file pyproject.toml
if [ $? != 0 ]; then
    exit 1
else
    echo "isort looks good!"
fi
echo

echo "> running pylint..."
pylint usfm_references

if [ $? != 0 ] && [ $? != 32 ]; then
    echo "Exit code: $?"
    exit 1
else
    echo "pylint looks good!"
fi
echo
