"""
USFM References Tools
"""

import re
import typing

__version__ = "1.4.0"

# Abbreviations provided by https://www.logos.com/bible-book-abbreviations
# Excluding periods on abbreviations, but functionality should allow it
# Also excluded abbreviations that match USFM id
BOOKS_DATA = {
    "GEN": {"abbreviations": ["ge", "gn"], "canon": "ot"},
    "EXO": {"abbreviations": ["ex", "exod"], "canon": "ot"},
    "LEV": {"abbreviations": ["le", "lv"], "canon": "ot"},
    "NUM": {"abbreviations": ["nu", "nm", "nb"], "canon": "ot"},
    "DEU": {"abbreviations": ["deut", "de", "dt"], "canon": "ot"},
    "JOS": {"abbreviations": ["josh", "jsh"], "canon": "ot"},
    "JDG": {"abbreviations": ["judg", "jg", "jdgs"], "canon": "ot"},
    "RUT": {"abbreviations": ["ru"], "canon": "ot"},
    "1SA": {
        "abbreviations": ["1 sam", "1 sm", "1 sa", "i sam", "i sa", "1sam", "1st sam", "first sam"],
        "canon": "ot",
    },
    "2SA": {
        "abbreviations": [
            "2 sam",
            "2 sm",
            "2 sa",
            "ii sam",
            "ii sa",
            "2sam",
            "2nd sam",
            "second sam",
        ],
        "canon": "ot",
    },
    "1KI": {
        "abbreviations": ["1 kgs", "1 ki", "1kgs", "1kin", "i kgs", "i ki", "1st kgs", "first Kgs"],
        "canon": "ot",
    },
    "2KI": {
        "abbreviations": [
            "2 kgs",
            "2 ki",
            "2kgs",
            "2kin",
            "ii kgs",
            "ii ki",
            "2nd kgs",
            "second kgs",
        ],
        "canon": "ot",
    },
    "1CH": {"abbreviations": ["1 chron",
"1 chr",
"1 ch",
"1chron",
"1chr",
"i chron",
"i chr",
"i ch",
"1st chron",
"first chron",], "canon": "ot"},
    "2CH": {"abbreviations": [ "chron",
"2 chr",
"2 ch",
"2chron",
"2chr",
"2ch",
"ii chron",
"ii chr",
"ii ch",
"2nd chronicles",
"2nd chron",
"second chronicles",
"second chron",], "canon": "ot"},
    "EZR": {"abbreviations": ["ezra",
"ez",
], "canon": "ot"},
    "NEH": {"abbreviations": [
"ne,"
], "canon": "ot"},
    "EST": {"abbreviations": [
"esth",
"es",
], "canon": "ot"},
    "JOB": {"abbreviations": ["jb",], "canon": "ot"},
    "PSA": {"abbreviations": ["ps",
"psalm",
"pslm",
"psm",
"pss",], "canon": "ot"},
    "PRO": {"abbreviations": ["prov",
"prv",
"pr",], "canon": "ot"},
    "ECC": {"abbreviations": ["eccles",
"eccle",
"ec",
"qoh",
], "canon": "ot"},
    "SNG": {"abbreviations": ["song",
"song of songs",
"sos",
"so",
"canticle of canticles",
"canticles",
"cant",
], "canon": "ot"},
    "ISA": {"abbreviations": ["is",], "canon": "ot"},
    "JER": {"abbreviations": ["je", "jr",], "canon": "ot"},
    "LAM": {"abbreviations": ["la",], "canon": "ot"},
    "EZK": {"abbreviations": ["ezek", "eze," ], "canon": "ot"},
    "DAN": {"abbreviations": ["da", "dn",], "canon": "ot"},
    "HOS": {"abbreviations": ["ho",], "canon": "ot"},
    "JOL": {"abbreviations": ["jl",], "canon": "ot"},
    "AMO": {"abbreviations": ["am",], "canon": "ot"},
    "OBA": {"abbreviations": ["obad", "ob",], "canon": "ot"},
    "JON": {"abbreviations": ["jnh",], "canon": "ot"},
    "MIC": {"abbreviations": ["mc",], "canon": "ot"},
    "NAM": {"abbreviations": ["na",], "canon": "ot"},
    "HAB": {"abbreviations": ["hb",], "canon": "ot"},
    "ZEP": {"abbreviations": ["zp", "zeph",], "canon": "ot"},
    "HAG": {"abbreviations": ["hg",], "canon": "ot"},
    "ZEC": {"abbreviations": ["zech", "zc",], "canon": "ot"},
    "MAL": {"abbreviations": ["ml",], "canon": "ot"},
    "MAT": {"abbreviations": ["matt", "mt",], "canon": "nt"},
    "MRK": {"abbreviations": ["mar", "mk", "mr",], "canon": "nt"},
    "LUK": {"abbreviations": ["lk"], "canon": "nt"},
    "JHN": {"abbreviations": ["jon", "jn",], "canon": "nt"},
    "ACT": {"abbreviations": ["ac",], "canon": "nt"},
    "ROM": {"abbreviations": ["ro",], "canon": "nt"},
    "1CO": {
        "abbreviations": ["1 cor", "1 co", "i cor", "i co", "1cor", "1corinthians"],
        "canon": "nt",
    },
    "2CO": {
        "abbreviations": ["2 cor", "2 co", "ii cor", "ii co", "2cor", "2corinthians"],
        "canon": "nt",
    },
    "GAL": {"abbreviations": ["ga"], "canon": "nt"},
    "EPH": {"abbreviations": ["ephes"], "canon": "nt"},
    "PHP": {"abbreviations": ["phil", "pp"], "canon": "nt"},
    "COL": {"abbreviations": ["co"], "canon": "nt"},
    "1TH": {
        "abbreviations": [
            "1 thess",
            "1 thes",
            "1 th",
            "i thess",
            "i thes",
            "i th",
            "1thessalonians",
            "1thess",
            "1thes",
            "1st thess",
            "first thess",
        ],
        "canon": "nt",
    },
    "2TH": {
        "abbreviations": [
            "2 thess",
            "2 thes",
            "2 th",
            "ii thess",
            "ii thes",
            "ii th",
            "2thessalonians",
            "2thess",
            "2thes",
            "2nd thess",
            "second thess",
        ],
        "canon": "nt",
    },
    "1TI": {
        "abbreviations": [
            "1 tim",
            "1 ti",
            "i tim",
            "i ti",
            "1timothy",
            "1tim",
            "1st tim",
            "first tim",
        ],
        "canon": "nt",
    },
    "2TI": {
        "abbreviations": [
            "2 tim",
            "2 ti",
            "ii tim",
            "ii ti",
            "2timothy",
            "2tim",
            "2nd Tim",
            "second tim",
        ],
        "canon": "nt",
    },
    "TIT": {"abbreviations": ["ti"], "canon": "nt"},
    "PHM": {"abbreviations": ["philem", "pm"], "canon": "nt"},
    "HEB": {"abbreviations": [], "canon": "nt"},
    "JAS": {"abbreviations": ["jm"], "canon": "nt"},
    "1PE": {
        "abbreviations": [
            "1 pet",
            "1 pe",
            "1 pt",
            "1 p",
            "i pet",
            "i pt",
            "i pe",
            "1peter",
            "1pet",
            "1pt",
            "1p",
        ],
        "canon": "nt",
    },
    "2PE": {
        "abbreviations": [
            "2 pet",
            "2 pe",
            "2 pt",
            "2 p",
            "ii pet",
            "ii pt",
            "ii pe",
            "2peter",
            "2pet",
            "2pt",
            "2p",
        ],
        "canon": "nt",
    },
    "1JN": {
        "abbreviations": [
            "1 jhn",
            "1 jn",
            "1 j",
            "1john",
            "1jhn",
            "1joh",
            "1jn",
            "1jo",
            "1j",
            "i jhn",
            "i joh",
            "i jn",
            "i jo",
        ],
        "canon": "nt",
    },
    "2JN": {
        "abbreviations": [
            "2 jhn",
            "2 jn",
            "2 j",
            "2john",
            "2jhn",
            "2joh",
            "2jn",
            "2jo",
            "2j",
            "ii jhn",
            "ii joh",
            "ii jn",
            "ii jo",
        ],
        "canon": "nt",
    },
    "3JN": {
        "abbreviations": [
            "3 jhn",
            "3 j",
            "3john",
            "3jhn",
            "3joh",
            "3jo",
            "3j",
            "iii john",
            "iii jhn",
            "iii joh",
            "iii jn",
            "iii jo",
        ],
        "canon": "nt",
    },
    "JUD": {"abbreviations": ["jd"], "canon": "nt"},
    "REV": {"abbreviations": ["re", "the revelation"], "canon": "nt"},
    "TOB": {"abbreviations": [], "canon": "ap"},
    "JDT": {"abbreviations": [], "canon": "ap"},
    "ESG": {"abbreviations": [], "canon": "ap"},
    "WIS": {"abbreviations": [], "canon": "ap"},
    "SIR": {"abbreviations": [], "canon": "ap"},
    "BAR": {"abbreviations": [], "canon": "ap"},
    "LJE": {"abbreviations": [], "canon": "ap"},
    "S3Y": {"abbreviations": [], "canon": "ap"},
    "SUS": {"abbreviations": [], "canon": "ap"},
    "BEL": {"abbreviations": [], "canon": "ap"},
    "1MA": {"abbreviations": [], "canon": "ap"},
    "2MA": {"abbreviations": [], "canon": "ap"},
    "3MA": {"abbreviations": [], "canon": "ap"},
    "4MA": {"abbreviations": [], "canon": "ap"},
    "1ES": {"abbreviations": [], "canon": "ap"},
    "2ES": {"abbreviations": [], "canon": "ap"},
    "MAN": {"abbreviations": [], "canon": "ap"},
    "PS2": {"abbreviations": [], "canon": "ap"},
    "ODA": {"abbreviations": [], "canon": "ap"},
    "PSS": {"abbreviations": [], "canon": "ap"},
    "3ES": {"abbreviations": [], "canon": "ap"},
    "EZA": {"abbreviations": [], "canon": "ap"},
    "5EZ": {"abbreviations": [], "canon": "ap"},
    "6EZ": {"abbreviations": [], "canon": "ap"},
    "DAG": {"abbreviations": [], "canon": "ap"},
    "PS3": {"abbreviations": [], "canon": "ap"},
    "2BA": {"abbreviations": [], "canon": "ap"},
    "LBA": {"abbreviations": [], "canon": "ap"},
    "JUB": {"abbreviations": [], "canon": "ap"},
    "ENO": {"abbreviations": [], "canon": "ap"},
    "1MQ": {"abbreviations": [], "canon": "ap"},
    "2MQ": {"abbreviations": [], "canon": "ap"},
    "3MQ": {"abbreviations": [], "canon": "ap"},
    "REP": {"abbreviations": [], "canon": "ap"},
    "4BA": {"abbreviations": [], "canon": "ap"},
    "LAO": {"abbreviations": [], "canon": "ap"},
    "LKA": {"abbreviations": [], "canon": "nt"},  # luke-acts combo
}

# Denormalized data
BOOKS = list(BOOKS_DATA.keys())
AP_BOOKS = [usfm for usfm, data in BOOKS_DATA.items() if data["canon"].lower() == "ap"]
NT_BOOKS = [usfm for usfm, data in BOOKS_DATA.items() if data["canon"].lower() == "nt"]
OT_BOOKS = [usfm for usfm, data in BOOKS_DATA.items() if data["canon"].lower() == "ot"]

# Validation regexes
ANY_REF = re.compile(r"^[1-9A-Z]{3}\.([0-9]{1,3}(_[0-9]+)?(\.[0-9]{1,3})?|INTRO\d+)$")
CHAPTER = re.compile(r"^[1-6A-Z]{3}\.[0-9]{1,3}(_[0-9]+)?$")
CHAPTER_OR_INTRO = re.compile(r"^[1-9A-Z]{3}\.([0-9]{1,3}(_[0-9]+)?|INTRO\d+)$")
SINGLE_CHAPTER_OR_VERSE = re.compile(r"^([A-Za-z]{3})\.([1-9]+\.{0,1}[1-9]*)$")
VERSE = re.compile(r"^[1-6A-Z]{3}\.[0-9]{1,3}(_[0-9]+)?\.[0-9]{1,3}$")
VERSE_RANGE = re.compile(r"^[\d\s]*[-\w\s]+\d+:\d+-\d+$")


def convert_book_to_canon(book_usfm: str) -> str:
    """Get the canon str from a book usfm."""
    return BOOKS_DATA.get(book_usfm, {}).get("canon", "ap")


# pylint: disable=inconsistent-return-statements
def convert_verse_range(ref: str) -> typing.Optional[list]:
    """Parse string to see if it is a range of verses."""
    if re.match(VERSE_RANGE, ref):
        book = re.findall(r"^([\d\s]*[-\w\s]+)\d+:\d+-\d+$", ref)[0]
        chapter = re.findall(r"^[\d\s]*[-\w\s]+(\d+):\d+-\d+$", ref)[0]
        first_verse = int(re.findall(r"^[\d\s]*[-\w\s]+\d+:(\d+)-\d+$", ref)[0])
        last_verse = int(re.findall(r"^[\d\s]*[-\w\s]+\d+:\d+-(\d+)$", ref)[0])

        hyphen_pos = ref.rfind("-")
        first_ref = ref[0:hyphen_pos]
        all_refs = [first_ref]
        for verse_number in range(first_verse + 1, last_verse + 1):
            all_refs.append(f"{book}{chapter}:{verse_number}")

        return all_refs


def valid_chapter(ref: str) -> bool:
    """
    Succeeds if the given string is a validly structured USFM Bible chapter reference.
    A valid, capitalized (English) book abbreviation,
        followed by a period (.) and a (chapter) number of any length,
        optionally followed by an underscore (_) and a (sub-chapter?) number of any length.
    """
    return bool(re.match(CHAPTER, ref) and ref.split(".")[0] in BOOKS)


def valid_chapter_or_intro(ref: str) -> bool:
    """
    Succeeds if the given string is a validly structured USFM Bible chapter reference or and INTRO.
    A valid, capitalized (English) book abbreviation,
        followed by a period (.) and a (chapter) number of any length,
        optionally followed by an underscore (_) and a (sub-chapter?) number of any length.
    OR
        followed by a period (.) and INTRO, followed by a number
    """
    return bool(CHAPTER_OR_INTRO.match(ref)) and ref.split(".")[0] in BOOKS


def valid_usfm(ref: str) -> bool:
    """
    Succeeds if the given string is a validly structured USFM Bible reference.
    A valid, capitalized (English) book abbreviation,
        followed by a period (.) and a (chapter) number of any length,
        optionally followed by an underscore (_) and a (sub-chapter?) number of any length,
        optionally followed by a period (.) and a (verse) number of any length.
    """
    return bool(ANY_REF.match(ref)) and ref.split(".")[0] in BOOKS


def valid_verse(ref: str) -> bool:
    """
    Succeeds if the given string is a validly structured USFM Bible verse reference.
    A valid, capitalized (English) book abbreviation,
        followed by a period (.) and a (chapter) number of any length,
        optionally followed by an underscore (_) and a (sub-chapter?) number of any length,
        optionally followed by a period (.) and a (verse) number of any length.
    """
    return bool(re.match(VERSE, ref) and ref.split(".")[0] in BOOKS)


def valid_multi_usfm(ref: str, delimiter: str = "+") -> bool:
    """
    Succeeds if the given string is a validly structured set of UFM Bible references.
    A valid, capitalized (English) book abbreviation,
        followed by a period (.) and a (chapter) number of any length,
        optionally followed by an underscore (_) and a (sub-chapter?) number of any length,
        optionally followed by a period (.) and a (verse) number of any length.
    Multiple verses are seperated by a plus (+)
    Example Multi USFM ref (James1:1-5): JAS.1.1+JAS.1.2+JAS.1.3+JAS.1.4+JAS.1.5
    Another Example with COMMA delimiter: JAS.1.1,JAS.1.2,JAS.1.3,JAS.1.4,JAS.1.5
    """
    if any(not valid_usfm(usfm) for usfm in ref.split(delimiter)):
        return False
    return True


def book_lookup(book_query):
    """Lookup a book USFM by a query."""
    # replace the following 2 lines by looking at all book abbreviations
    if book_query == "Matt":
        return "MAT"
    if book_query in BOOKS or book_query.upper() in BOOKS:
        return book_query.upper()
