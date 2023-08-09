from crossref.restful import Works
from get_pmid_information import get_pmid_citation, get_pmid_information, PMIDRequestException
from get_doi_information import doi_crossref_search


def create_reference(ref_type, value):
    if ref_type == "DOI":
        doi_information = doi_crossref_search(value)
        return doi_information

    elif ref_type == "PMID":

        # Get the reference information from the pmid
        try:
            pmid_information = get_pmid_information(value)
        except ValueError as e:
            pmid_information = None

        # Get the full citation from the pmid
        try:
            pmid_reference = get_pmid_citation(value)
        except PMIDRequestException as e:
            pmid_reference = None

        if pmid_reference is not None and pmid_information is not None:
            return {
                "title": pmid_information["title"],
                "year": pmid_information["year"],
                "journal": pmid_information["journal"],
                "volume": pmid_information["volume"],
                "citation": pmid_reference
            }
        else:
            return None



