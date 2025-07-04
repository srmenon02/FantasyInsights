import pandas as pd
from bs4 import BeautifulSoup
from .utils import fetch_url


TEAM_ABBR_MAP = {
    "San Francisco 49ers": "sfo",
    "Chicago Bears": "chi",
    "Cincinnati Bengals": "cin",
    "Buffalo Bills": "buf",
    "Denver Broncos": "den",
    "Cleveland Browns": "cle",
    "Tampa Bay Buccaneers": "tam",
    "Arizona Cardinals": "crd",
    "Los Angeles Chargers": "sdg",
    "Kansas City Chiefs": "kan",
    "Indianapolis Colts": "clt",
    "Washington Commanders": "was",
    "Dallas Cowboys": "dal",
    "Miami Dolphins": "mia",
    "Philadelphia Eagles": "phi",
    "Atlanta Falcons": "atl",
    "New York Giants": "nyg",
    "Jacksonville Jaguars": "jax",
    "New York Jets": "nyj",
    "Detroit Lions": "det",
    "Green Bay Packers": "gnb",
    "Carolina Panthers": "car",
    "New England Patriots": "nwe",
    "Las Vegas Raiders": "rai",
    "Los Angeles Rams": "ram",
    "Baltimore Ravens": "rav",
    "New Orleans Saints": "nor",
    "Seattle Seahawks": "sea",
    "Pittsburgh Steelers": "pit",
    "Houston Texans": "htx",
    "Tennessee Titans": "oti",
    "Minnesota Vikings": "min"
}
def get_season_games(year=2024):
    """
    Scrape season schedule and return a DataFrame with games, dates, and box score URLs.
    """
    url = f"https://www.pro-football-reference.com/years/{year}/games.htm"
    html = fetch_url(url)
    soup = BeautifulSoup(html, "html.parser")

    table = soup.find("table", id="games")
    if table is None:
        raise ValueError("Could not find games table on the page.")

    df = pd.read_html(str(table))[0]

    # Remove repeated header rows within the table (sometimes 'Week' string appears)
    df = df[df['Week'].apply(lambda x: str(x).isdigit())]
    
    df.rename(columns={df.columns[5]: 'Location'}, inplace=True)
    # Convert date column to datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # Build BoxScoreURL for each game
    def build_boxscore_url(row):
        # URL format: /boxscores/YYYYMMDD0TEAM.htm
        date_str = row['Date'].strftime('%Y%m%d')
        # Use winner team abbreviation for URL - get first 3 letters uppercase, no spaces
        abbr = TEAM_ABBR_MAP[row['Loser/tie']] if row['Location'] == '@' else TEAM_ABBR_MAP[row['Winner/tie']]
        return f"https://www.pro-football-reference.com/boxscores/{date_str}0{abbr}.htm#"

    df['BoxScoreURL'] = df.apply(build_boxscore_url, axis=1)

    return df[['Week', 'Date', 'Winner/tie', 'Loser/tie', 'BoxScoreURL']]
