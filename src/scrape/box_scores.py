import pandas as pd
from bs4 import BeautifulSoup
from .utils import fetch_url
from io import StringIO

def scrape_box_score(url):
    """
    Scrape box score page and return a dict of DataFrames keyed by team or stat name.
    Example keys: 'Passing', 'Rushing', 'Receiving', 'Defense', etc.
    """
    html = fetch_url(url)
    soup = BeautifulSoup(html, "html.parser")

    # All tables on the page
    tables = soup.find_all("table")

    stats = {}

    for table in tables:
        table_id = table.get('id')
        if not table_id:
            continue  # skip tables without ID

        # Parse table into DataFrame
        df = pd.read_html(StringIO(str(table)))[0]

        # Remove repeated header rows within the table
        df = df[df[df.columns[0]] != df.columns[0]]

        # Reset index
        df.reset_index(drop=True, inplace=True)

        stats[table_id] = df

    return stats
