import pandas as pd
import os

# Set the directory where CSV files are stored
csv_directory = "C:/Users/luk/Orininu Streaming Service/export_csv"

# List of all tables to convert
tables = ["users", "artists", "albums", "songs", "user_interaction", "playlists", "playlist_songs"]

# Convert CSVs to JSON and save them in the same folder
for table in tables:
    csv_path = os.path.join(csv_directory, f"{table}.csv")
    json_path = os.path.join(csv_directory, f"{table}.json")

    # Load CSV file
    df = pd.read_csv(csv_path)

    # Convert to JSON format
    json_data = df.to_json(orient="records")

    # Save JSON file
    with open(json_path, "w") as f:
        f.write(json_data)

    print(f"✅ Converted {table}.csv → {table}.json")
