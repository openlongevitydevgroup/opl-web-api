from open_problems.models.references import Reference, Journal
from typing import Union


def validate_submitted_reference(title: str, year: str) -> bool:
    """
    Checks whether a reference with the given title and year already exists in the database.

    Args:
        title (str): Title of the reference.
        year (int): Year of the reference publication.

    Returns:
        bool: True if a matching reference exists, False otherwise.
    """
    return Reference.objects.filter(ref_title=title, publish_date=year).exists()


def validate_journal(journal_name: str) -> Union[object, bool]:
    """
    Check whether a journal with the given name exists in the database.

    Args:
        journal_name (str): The name of the journal to validate.

    Returns:
        int or False: The primary key (ID) of the journal if it exists, or False if it doesn't.
    """
    if Journal.objects.filter(journal_name=journal_name).exists():
        journal = Journal.objects.filter(journal_name=journal_name).first()
        return journal
    else:
        return False
