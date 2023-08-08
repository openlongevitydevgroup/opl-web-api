from crossref.restful import Works
import requests
from xml.etree import ElementTree as ET


def get_pubmed_info(pubmed_id):
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    endpoint = "efetch.fcgi"
    db = "pubmed"
    retmode = "xml"

    url = f"{base_url}{endpoint}?db={db}&id={pubmed_id}&retmode={retmode}"
    response = requests.get(url)

    if response.status_code == 200:
        root = ET.fromstring(response.text)

        title = root.find(".//ArticleTitle").text
        year = root.find(".//PubDate/Year").text
        journal = root.find(".//Title").text

        full_text_citation = f"{title}. {year}. {journal}."

        return {
            "full_text_citation": full_text_citation,
            "title": title,
            "year": year,
            "journal": journal
        }
    else:
        return ValueError("Failed API Call to Entrez")

def format_harvard(data):
    authors = data['author']
    year = data['published-print']['date-parts'][0][0]
    title = data['title'][0]
    journal = data['short-container-title'][0]
    volume = data['volume']
    issue = data['issue']
    pages = data['page']
    publisher = data['publisher']
    doi = data['DOI']

    author_list = ', '.join([f"{author['family']}, {author['given'][0]}." for author in authors])

    citation = f"{author_list} ({year}) \"{title}.\" *{journal}*, {volume}({issue}), {pages}. {publisher}. doi:{doi}"
    return title, year, journal, volume, citation


def create_reference(ref_type, value):
    if ref_type == "DOI":
        works = Works()
        try:
            search = works.doi(value)
        except TypeError:
            return None
        else:
            title, year, journal, volume, citation = format_harvard(search)
            return title, year, journal, volume,citation

    elif ref_type == "PMID":
        ...


ref_type = "DOI"
value = "10.1016/j.cell.2013.05.03"

if __name__ == "__main__":
    create_reference(ref_type, value)
