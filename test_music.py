from music import create_artist_folder, move_album_to_artist_folder, remove_artist_name_from_album, check_song_extension, check_song_contains_name, check_song_number
import os

def test_create_artist_folder():
    artist_name = 'The Beatles'
    artist_folder = create_artist_folder(artist_name)
    assert os.path.exists(artist_folder)
    assert os.path.isdir(artist_folder)
    assert artist_name in artist_folder

def test_move_album_to_artist_folder():
    artist_name = 'The Beatles'
    artist_folder = create_artist_folder(artist_name)
    album_name = 'The Beatles - Abbey Road'
    album_folder = os.path.join(os.getcwd(), album_name)
    os.makedirs(album_folder)
    destination_folder = move_album_to_artist_folder(artist_folder, album_folder)
    assert os.path.exists(destination_folder)
    assert os.path.isdir(destination_folder)
    assert album_name in destination_folder
    assert not os.path.exists(album_folder)

def test_remove_artist_name_from_album():
    artist_name = 'The Beatles'
    album_name = 'The Beatles - Abbey Road'
    album_folder = os.path.join(os.getcwd(), album_name)
    os.makedirs(album_folder)
    new_album_folder = remove_artist_name_from_album(album_folder, artist_name)
    assert os.path.exists(new_album_folder)
    assert os.path.isdir(new_album_folder)
    assert album_name.replace(artist_name + ' - ', '') in new_album_folder
    assert not os.path.exists(album_folder)

def test_check_song_extension():
    song_name = 'song.mp3'
    song_path = os.path.join(os.getcwd(), song_name)
    with open(song_path, 'w') as f:
        f.write('test')
    check_song_extension(song_path)
    assert os.path.exists(song_path)
    assert os.path.isfile(song_path)
    os.remove(song_path)

def test_check_song_contains_name():
    song_name = 'The Beatles - Abbey Road - 01 - Come Together.mp3'
    song_path = os.path.join(os.getcwd(), song_name)
    with open(song_path, 'w') as f:
        f.write('test')
    artist_name = 'The Beatles'
    check_song_contains_name(song_path, artist_name)
    assert os.path.exists(song_path)
    assert os.path.isfile(song_path)
    os.remove(song_path)

def test_check_song_number():
    song_name = 'The Beatles - Abbey Road - 01 - Come Together.mp3'
    song_path = os.path.join(os.getcwd(), song_name)
    with open(song_path, 'w') as f:
        f.write('test')
    check_song_number(song_path)
    assert os.path.exists(song_path)
    assert os.path.isfile(song_path)
    os.remove(song_path)