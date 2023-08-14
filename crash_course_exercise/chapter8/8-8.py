def make_album(artist, title, num_tracks=None):
    album = {
        'artist': artist,
        'title': title,
    }
    if num_tracks is not None:
        album['num_tracks'] = num_tracks
    return album


while True:
    print("Enter album information (or 'q' to quit):")
    artist = input("Artist: ")
    if artist.lower() == 'q':
        break

    title = input("Album Title: ")
    if title.lower() == 'q':
        break

    num_tracks_input = input(
        "Number of Tracks (optional, press Enter to skip): ")
    if num_tracks_input.lower() == 'q':
        break

    if num_tracks_input:
        try:
            num_tracks = int(num_tracks_input)
        except ValueError:
            print("Invalid input for number of tracks. Skipping...")
            num_tracks = None
    else:
        num_tracks = None

    album = make_album(artist, title, num_tracks)
    print("Album information:")
    print(album)
