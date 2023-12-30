import sys
import os
import shutil
import re

current_script = os.path.basename(__file__)

def main():
    try:
        if len(sys.argv) == 1:
            raise Exception("No arguments provided")
        elif len(sys.argv) == 2:
            if sys.argv[1] == "-h" or sys.argv[1] == "--help":
                print("Thank you for using music.py")
                print("Use -v or --version to get the version")
                print("Use -a or --author to get the author")
                print("Use artists or --artists to arrange your music by artist")
                print("Use albums or --albums to arrange your music by album")
                print("Use songs or --songs to arrange your music by songs")
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
            elif sys.argv[1] == "all" or sys.argv[1] == "--all":
                print("Executing Artist arrangement")
                handle_artists()
                print("Executing Album arrangement")
                handle_albums()
                print("Executing Song arrangement")
                handle_songs()
            else:
                raise Exception("Invalid argument")
    except Exception as e:
        print(e)
        print("Use -h or --help for help")
        sys.exit(1)

def handle_artists():
    music_folder = os.getcwd()
    for item in os.listdir(music_folder):
        if item == current_script:
            continue
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
        if artist == current_script:
            continue
        artist_path = os.path.join(music_folder, artist)
        artist_name = os.path.basename(artist_path)
        for album in os.listdir(artist_path):
            album_path = os.path.join(artist_path, album)

            try:
                if os.path.isdir(album_path) and not album.startswith('.'):
                    if artist_name in album:
                        album_folder = remove_artist_name_from_album(album_path, artist_name)
                        print("Removed artist name from {}".format(album_folder))
            except (OSError, IOError) as e:
                print("Error processing {}: {}".format(album_path, e))
                continue
    
def remove_artist_name_from_album(album_folder, artist_name):
    album_name = album_folder.replace(artist_name + ' - ', '')
    new_album_folder = os.path.join(os.path.dirname(album_folder), album_name)
    os.rename(album_folder, new_album_folder)
    return new_album_folder

def handle_songs():
    music_folder = os.getcwd()
    for artist in os.listdir(music_folder):
        if artist == current_script:
            continue
        artist_path = os.path.join(music_folder, artist)
        artist_name = os.path.basename(artist_path)
        for album in os.listdir(artist_path):
            album_path = os.path.join(artist_path, album)
            album_name = os.path.basename(album_path)
            check_song_number(album_path)
            for song in os.listdir(album_path):
                song_path = os.path.join(album_path, song)
                try:
                    if os.path.isfile(song_path):
                        check_song_contains_name(song_path, artist_name)
                        check_song_contains_name(song_path, album_name)
                        check_song_extension(song_path)
                except (OSError, IOError) as e:
                    print("Error processing {}: {}".format(song_path, e))
                    continue


def check_song_extension(song_path):
    song_name, song_extension = os.path.splitext(song_path)
    if song_extension in song_name:
        new_song_path = song_name.replace(song_extension, '') + song_extension
        os.rename(song_path, new_song_path)
        print("Renamed {} to {}".format(song_path, new_song_path))

def check_song_number(song_path):
    song_name, song_extension = os.path.splitext(song_path)
    pattern = re.compile(r'^(\d{2}) - (.+\.\w+)$')
    match = pattern.match(song_name)
    if match:
        track_number, track_name = match.groups()
        track_number = int(track_number)
        new_song_name = f"{track_number:02d} - {track_name}"
        new_song_path = os.path.join(os.path.dirname(song_path), new_song_name + song_extension)
        os.rename(song_path, new_song_path)
        print(f"Renamed: {song_path} -> {new_song_path}")


def check_song_contains_name(song_path, name):
    song_name, song_extension = os.path.splitext(song_path)
    if name in song_name:
        new_song_path = song_name.replace(name, '') + song_extension
        new_song_path = os.path.join(os.path.dirname(song_path), new_song_path)
        os.rename(song_path, new_song_path)
        print("Renamed {} to {}".format(song_path, new_song_path))
    

if __name__ == "__main__":
    main()