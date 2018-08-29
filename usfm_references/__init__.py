"""
USFM References Tools
"""
import re

__version__ = '1.0.2'

ANY_REF = re.compile(r'^[1-9A-Z]{3}\.([0-9]{1,3}(_[0-9]+)?(\.[0-9]{1,3})?|INTRO\d+)$')
CHAPTER = re.compile(r'^[1-6A-Z]{3}\.[0-9]{1,3}(_[0-9]+)?$')
CHAPTER_OR_INTRO = re.compile(r'^[1-9A-Z]{3}\.([0-9]{1,3}(_[0-9]+)?|INTRO\d+)$')
SINGLE_CHAPTER_OR_VERSE = re.compile(r'^([A-Za-z]{3})\.([1-9]+\.{0,1}[1-9]*)$')
VERSE = re.compile(r'^[1-6A-Z]{3}\.[0-9]{1,3}(_[0-9]+)?\.[0-9]{1,3}$')
BOOKS = [
    'GEN', 'EXO', 'LEV', 'NUM', 'DEU', 'JOS', 'JDG', 'RUT', '1SA', '2SA', '1KI', '2KI', '1CH',
    '2CH', 'EZR', 'NEH', 'EST', 'JOB', 'PSA', 'PRO', 'ECC', 'SNG', 'ISA', 'JER', 'LAM', 'EZK',
    'DAN', 'HOS', 'JOL', 'AMO', 'OBA', 'JON', 'MIC', 'NAM', 'HAB', 'ZEP', 'HAG', 'ZEC', 'MAL',
    'MAT', 'MRK', 'LUK', 'JHN', 'ACT', 'ROM', '1CO', '2CO', 'GAL', 'EPH', 'PHP', 'COL', '1TH',
    '2TH', '1TI', '2TI', 'TIT', 'PHM', 'HEB', 'JAS', '1PE', '2PE', '1JN', '2JN', '3JN', 'JUD',
    'REV', 'TOB', 'JDT', 'ESG', 'WIS', 'SIR', 'BAR', 'LJE', 'S3Y', 'SUS', 'BEL', '1MA', '2MA',
    '3MA', '4MA', '1ES', '2ES', 'MAN', 'PS2', 'ODA', 'PSS', 'EZA', '5EZ', '6EZ', 'DAG', 'PS3',
    '2BA', 'LBA', '2MQ', '3MQ', 'REP', '4BA', 'LAO', 'LKA'
]


def valid_chapter(ref):
    """
    Succeeds if the given string is a validly structured USFM Bible chapter reference.
    A valid, capitalized (English) book abbreviation,
        followed by a period (.) and a (chapter) number of any length,
        optionally followed by an underscore (_) and a (sub-chapter?) number of any length.
    """
    return bool(re.match(CHAPTER, ref) and ref.split('.')[0] in BOOKS)


def valid_chapter_or_intro(ref):
    """
    Succeeds if the given string is a validly structured USFM Bible chapter reference or and INTRO.
    A valid, capitalized (English) book abbreviation,
        followed by a period (.) and a (chapter) number of any length,
        optionally followed by an underscore (_) and a (sub-chapter?) number of any length.
    OR
        followed by a period (.) and INTRO, followed by a number
    """
    return bool(CHAPTER_OR_INTRO.match(ref)) and ref.split('.')[0] in BOOKS


def valid_usfm(ref):
    """
    Succeeds if the given string is a validly structured USFM Bible reference.
    A valid, capitalized (English) book abbreviation,
        followed by a period (.) and a (chapter) number of any length,
        optionally followed by an underscore (_) and a (sub-chapter?) number of any length,
        optionally followed by a period (.) and a (verse) number of any length.
    """
    return bool(ANY_REF.match(ref)) and ref.split('.')[0] in BOOKS


def valid_verse(ref):
    """
    Succeeds if the given string is a validly structured USFM Bible verse reference.
    A valid, capitalized (English) book abbreviation,
        followed by a period (.) and a (chapter) number of any length,
        optionally followed by an underscore (_) and a (sub-chapter?) number of any length,
        optionally followed by a period (.) and a (verse) number of any length.
    """
    return bool(re.match(VERSE, ref) and ref.split('.')[0] in BOOKS)
