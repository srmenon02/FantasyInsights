import pandas as pd
import time
import requests
from io import StringIO

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; FantasyBot/1.0; +https://github.com/srmenon02)"
}

def scrape_rb_rushing(year=2023):
    url = f"https://www.pro-football-reference.com/years/{year}/rushing.htm"
    print(f"Scraping RB rushing stats from {url}...")
    
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()

    tables = pd.read_html(StringIO(response.text))
    rushing_df = tables[0]
    rushing_df.columns = rushing_df.columns.get_level_values(1)
    rushing_df = rushing_df[rushing_df['Player'] != 'Player']  
    rushing_df = rushing_df.fillna(0)
    rushing_df.reset_index(drop=True, inplace=True)
    
    print(f"Found {len(rushing_df)} players in RB rushing stats")
    return rushing_df

def scrape_player_game_logs(player_id, year=2023):
    """
    Scrape individual player's game log for a season.
    player_id example: 'CookDa00' for Dalvin Cook
    """
    url = f"https://www.pro-football-reference.com/players/{player_id[0]}/{player_id}/gamelog/{year}/"
    print(f"Scraping game logs for player {player_id} from {url}...")

    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
    except requests.HTTPError as e:
        print(f"Failed to retrieve data for {player_id}: {e}")
        return pd.DataFrame()  # Return empty DataFrame on fail

    tables = pd.read_html(StringIO(response.text))
    game_log_df = tables[0]
    game_log_df = game_log_df[game_log_df['Week'] != 'Week']  # Remove repeated headers inside table
    game_log_df = game_log_df.fillna(0)
    game_log_df.reset_index(drop=True, inplace=True)
    
    # Add player_id column for later merging
    game_log_df['player_id'] = player_id
    return game_log_df

def save_df_to_csv(df, filepath):
    df.to_csv(filepath, index=False)
    print(f"Saved data to {filepath}")

def main():
    year = 2024

    # Step 1: Scrape all RB rushing stats
    rushing_df = scrape_rb_rushing(year)
    save_df_to_csv(rushing_df, f"../data/rb_rushing_{year}.csv")

    # Step 2: Scrape individual player game logs
    # Get list of player IDs from rushing_df Player column + some cleaning
    # Player URLs are based on a unique ID that you need to map yourself.
    # For demo, here are a few known RB player IDs:
    player_ids = [
        "CookDa00",  # Dalvin Cook
        "HenryDe01", # Derrick Henry
        "ElliSa00",  # Saquon Barkley
    ]

    all_game_logs = []

    for pid in player_ids:
        logs_df = scrape_player_game_logs(pid, year)
        if not logs_df.empty:
            all_game_logs.append(logs_df)
        time.sleep(1)  

    if all_game_logs:
        combined_logs = pd.concat(all_game_logs, ignore_index=True)
        save_df_to_csv(combined_logs, f"../data/player_game_logs_{year}.csv")
    else:
        print("No player game logs scraped.")

if __name__ == "__main__":
    main()
