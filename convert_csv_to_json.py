import pandas as pd
import os

csv_directory = "C:/Users/luk/Orininu Streaming Service/export_and_convert_csv"

# List of all tables to convert
tables = ["users", "artists", "albums", "songs", "user_interaction", "playlists", "playlist_songs"]

# Converting CSVs to JSON
for table in tables:
    csv_path = os.path.join(csv_directory, f"{table}.csv")
    json_path = os.path.join(csv_directory, f"{table}.json")

   
    df = pd.read_csv(csv_path)
    
    json_data = df.to_json(orient="records")

    # Saving JSON file
    with open(json_path, "w") as f:
        f.write(json_data)

    print(f"✅ Converted {table}.csv → {table}.json")
