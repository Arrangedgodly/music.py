import os
import shutil

def is_artist_album_folder(folder_name):
    parts = folder_name.split(" - ")
    if len(parts) == 2:
        return True
    else:
        return False

def main():
    current_dir = os.getcwd()
    for root, dirs, files in os.walk(current_dir):
        for dir in dirs:
            if is_artist_album_folder(dir):
                artist_name, album_name = dir.split(" - ")
                if not check_existing(artist_name):
                    os.mkdir(artist_name)
                    shutil.move(dir, artist_name)
                    os.chdir(artist_name)
                    os.rename(dir, album_name)
                    os.chdir(album_name)
                    for track in os.listdir():
                        if track.endswith(".mp3") or track.endswith(".flac"):
                            track_artist, track_album, track_title = track.split(" - ")
                            new_track_title = track_title.strip()
                            os.rename(track, new_track_title)
                else:
                    shutil.move(dir, artist_name)
                    os.chdir(artist_name)
                    os.rename(dir, album_name)
                    os.chdir(album_name)
                    for track in os.listdir():
                        if track.endswith(".mp3") or track.endswith(".flac"):
                            track_artist, track_album, track_title = track.split(" - ")
                            new_track_title = track_title.strip()
                            os.rename(track, new_track_title)
            else:
                continue

def check_existing(directory):
    if os.path.exists(directory):
        return True
    else:
        return False


if __name__ == '__main__':
    main()