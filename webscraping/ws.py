import requests
from bs4 import BeautifulSoup


def get_citations_needed_count(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    citation_tags = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
    return len(citation_tags)
    """
    Count the number of citations needed in a Wikipedia page.

    Args:
        url (str): The URL of the Wikipedia page.

    Returns:
        int: The number of citations needed in the page.
    """

def get_citations_needed_report(url):
    """
    Generate a report of passages that need citations in a Wikipedia page.

    Args:
        url (str): The URL of the Wikipedia page.

    Returns:
        str: The report containing the relevant passages that need citations.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    citation_tags = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')

    report = ''
    for tag in citation_tags:
        passage = tag.find_parent('p')
        report += passage.text.strip() + '\n'

    return report


# Example usage
url = 'https://en.wikipedia.org/wiki/History_of_Mexico'
citations_count = get_citations_needed_count(url)
report = get_citations_needed_report(url)

print(f"Number of citations needed: {citations_count}")
print("Citations needed report:")
print(report)