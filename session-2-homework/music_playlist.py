from datetime import datetime

def create_playlist():
    print("--- 🎧 Music Playlist Manager ---")
    
    # 1. Setup metadata
    playlist_name = input("Enter a name for your playlist: ")
    vibe = input("What's the vibe? (e.g., Chill, Party, Study, Sad): ")
    creation_date = datetime.now().strftime("%b %d, %Y")
    
    # 2. Collect songs using a List of Dictionaries
    playlist_storage = []
    
    print("\nEnter your songs (type 'done' when finished):")
    while True:
        song = input("\nSong Name: ")
        if song.lower() == 'done':
            break
        artist = input("Artist Name: ")
        
        # Adding a dictionary to our list
        playlist_storage.append({"title": song, "artist": artist})
    
    # 3. Formatting and Saving to File
    filename = f"{playlist_name.replace(' ', '_').lower()}.txt"
    
    try:
        with open(filename, "w", encoding="utf-8") as f:
            # Creative Header
            f.write("╔" + "═"*50 + "╗\n")
            f.write(f"║ {playlist_name.upper():^48} ║\n")
            f.write(f"║ Vibe: {vibe:<41}  ║\n")
            f.write(f"║ Date: {creation_date:<41}  ║\n")
            f.write("╚" + "═"*50 + "╝\n\n")
            
            f.write(f"{'#':<4} {'SONG TITLE':<25} {'ARTIST':<20}\n")
            f.write("-" * 52 + "\n")
            
            # Use enumerate to get the song number automatically
            for i, entry in enumerate(playlist_storage, 1):
                f.write(f"{i:<4} {entry['title']:<25} {entry['artist']:<20}\n")
                
            f.write("-" * 52 + "\n")
            f.write(f"Total Tracks: {len(playlist_storage)}\n")
            
        print(f"\n🎵 Rock on! Your playlist is saved in '{filename}'.")

    except Exception as e:
        print(f"Error saving playlist: {e}")

if __name__ == "__main__":
    create_playlist()