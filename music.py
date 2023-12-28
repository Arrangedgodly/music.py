import sys
import os
import shutil
import re

def main():
    if len(sys.argv) == 1:
        raise Exception("No arguments provided")
    elif len(sys.argv) == 2:
        if sys.argv[1] == "-h" or sys.argv[1] == "--help":
            print("Usage: python3 music.py <path to music folder>")
            sys.exit(0)
        elif sys.argv[1] == "-v" or sys.argv[1] == "--version":
            print("music.py 1.1.0")
            sys.exit(0)
        elif sys.argv[1] == "-a" or sys.argv[1] == "--author":
            print("Author: Graydon Wasil")
            sys.exit(0)
        elif sys.argv[1] == "artists" or sys.argv[1] == "--artists":
            print("Executing Artist arrangement")
            handle_artists()
        elif sys.argv[1] == "albums" or sys.argv[1] == "--albums":
            print("Executing Album arrangement")
            handle_albums()
        elif sys.argv[1] == "songs" or sys.argv[1] == "--songs":
            print("Executing Song arrangement")
            handle_songs()
        else:
            raise Exception("Invalid argument")

def handle_artists():
    music_folder = os.getcwd()
    for item in os.listdir(music_folder):
        item_path = os.path.join(music_folder, item)
        if os.path.isdir(item_path):
            if ' - ' in item:
                artist_name, album_name = item.split(' - ', 1)
                artist_folder = create_artist_folder(artist_name)
                album_folder = move_album_to_artist_folder(artist_folder, item_path)
                print("Moved {} to {}".format(album_folder, artist_folder))

def create_artist_folder(artist_name):
    artist_folder = os.path.join(os.getcwd(), artist_name)
    if not os.path.exists(artist_folder):
        os.makedirs(artist_folder)
    return artist_folder

def move_album_to_artist_folder(artist_folder, album_folder):
    destination_folder = os.path.join(artist_folder, os.path.basename(album_folder))
    shutil.move(album_folder, destination_folder)
    return destination_folder

def handle_albums():
    music_folder = os.getcwd()
    for artist in os.listdir(music_folder):
        artist_path = os.path.join(music_folder, artist)
        artist_name = os.path.basename(artist_path)
        for album in os.listdir(artist):
            album_path = os.path.join(music_folder, artist, album)
            if os.path.isdir(album_path):
                if artist_name in album:
                    album_folder = remove_artist_name_from_album(album_path, artist_name)
                    print("Removed artist name from {}".format(album_folder))
    
def remove_artist_name_from_album(album_folder, artist_name):
    album_name = album_folder.replace(artist_name, '')
    new_album_folder = os.path.join(os.path.dirname(album_folder), album_name)
    os.rename(album_folder, new_album_folder)
    return new_album_folder

def handle_songs():
    music_folder = os.getcwd()
    for artist in os.listdir(music_folder):
        artist_path = os.path.join(music_folder, artist)
        artist_name = os.path.basename(artist_path)
        for album in os.listdir(artist_path):
            album_path = os.path.join(artist_path, album)
            album_name = os.path.basename(album_path)
            for song in os.listdir(album_path):
                song_path = os.path.join(album_path, song)
                if os.path.isfile(song_path):
                    check_song_number(song_path)
                    check_song_contains_name(song_path, artist_name)
                    check_song_contains_name(song_path, album_name)
                    check_song_extension(song_path)

def check_song_extension(song_path):
    song_name, song_extension = os.path.splitext(song_path)
    if song_extension in song_name:
        new_song_path = song_name.replace(song_extension, '') + song_extension
        os.rename(song_path, new_song_path)
        print("Renamed {} to {}".format(song_path, new_song_path))

def check_song_number(album_path):
    songs = os.listdir(album_path)
    for index, song in enumerate(songs, start=1):
        song_path = os.path.join(album_path, song)
        song_name, song_extension = os.path.splitext(song_path)
        pattern = re.compile(r'^(\d{2}) - (.+\.\w+)$')
        match = pattern.match(song_name)
        if match:
                track_number, track_name = match.groups()
                track_number = int(track_number)
                if track_number != (index + 1):
                    new_song_name = f"{(index + 1):02d} - {track_name}" 
                    new_song_path = os.path.join(album_path, new_song_name)
                    os.rename(os.path.join(album_path, song_name), new_song_path)
                    print(f"Renamed: {song_name} -> {new_song_name}")

def check_song_contains_name(song_path, name):
    song_name, song_extension = os.path.splitext(song_path)
    if name in song_name:
        new_song_path = song_name.replace(name, '') + song_extension
        os.rename(song_path, new_song_path)
        print("Renamed {} to {}".format(song_path, new_song_path))
    

if __name__ == "__main__":
    main()