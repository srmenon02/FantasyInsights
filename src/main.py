from scrape import schedule, box_scores
import os
import pandas as pd
import time

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
os.makedirs(DATA_DIR, exist_ok=True)

def main(year=2024):
    print(f"Scraping season schedule for {year}...")
    games = schedule.get_season_games(year)
    print(f"Found {len(games)} games.")

    box_scores_data = []

    for idx, game in games.iterrows():
        time.sleep(3)
        url = game['BoxScoreURL']
        #url2 = game['BoxScoreURL'][1]
        #url=url1
        print(f"Scraping box score for game on {game['Date'].date()} {game['Winner/tie']} vs {game['Loser/tie']}")
        try:
            stats = box_scores.scrape_box_score(url)
            game_id = url.split("/")[-1].replace(".htm", "")
            game_folder = os.path.join(DATA_DIR, "box_scores", str(year))
            os.makedirs(game_folder, exist_ok=True)

            for stat_name, df in stats.items():
                file_path = os.path.join(game_folder, f"{game_id}_{stat_name}.csv")
                df.to_csv(file_path, index=False)

            box_scores_data.append((game_id, stats))
        except Exception as e:
            print(f"Error scraping {url}: {e}")

    print("Scraping complete.")

if __name__ == "__main__":
    main()
