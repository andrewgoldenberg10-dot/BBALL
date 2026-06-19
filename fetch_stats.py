import json
import time
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats

# 1. Get a list of all active NBA players
active_players = players.get_active_players()

compiled_players = []

# 2. Loop through the players to grab their current season averages
# Note: We limit this to the first 30 players for testing so you don't get blocked
for person in active_players[:30]:
    try:
        print(f"Fetching stats for {person['full_name']}...")
        
        # Pull career stats
        career = playercareerstats.PlayerCareerStats(player_id=person['id'])
        df = career.get_data_frames()[0]
        
        # Filter for the most recent regular season data row
        if not df.empty:
            latest_season = df.iloc[-1] 
            
            # NBA.com gives totals, so we divide by Games Played (GP) to get averages
            gp = latest_season['GP']
            if gp > 0:
                compiled_players.append({
                    "id": person['id'],
                    "name": person['full_name'],
                    "pts": round(latest_season['PTS'] / gp, 1),
                    "reb": round(latest_season['REB'] / gp, 1),
                    "ast": round(latest_season['AST'] / gp, 1)
                })
                
        # Crucial: Sleep for 1 second so NBA.com doesn't ban your IP address!
        time.sleep(1)
        
    except Exception as e:
        print(f"Skipped {person['full_name']} due to an error.")
        continue

# 3. Save it directly to a file your website can use
with open('players.json', 'w') as f:
    json.dump(compiled_players, f, indent=4)

print("Successfully generated players.json!")
