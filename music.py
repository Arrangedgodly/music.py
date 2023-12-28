import sys
import os

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

def handle_albums():

def handle_songs():

if __name__ == "__main__":
    main()