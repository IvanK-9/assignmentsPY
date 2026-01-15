def make_album(artist, title, songs=None):
    """like exc. 8‑7."""
    album = {'artist': artist, 'title': title}
    if songs is not None:
        album['songs'] = songs
    return album

print("Enter album information (type 'quit' to exit):")

while True:
    # 
    artist = input("\nArtist name: ")
    if artist.lower() == 'quit':
        break

    # 
    title = input("Album title: ")
    if title.lower() == 'quit':
        break

    # 
    song_input = input("Number of songs (or press Enter to skip): ")
    if song_input.lower() == 'quit':
        break
    elif song_input.strip() == '':  # 
        songs = None
    else:
        songs = int(song_input)

    # packing album and exit
    album = make_album(artist, title, songs)
    print("\nCreated album:")
    print(album)
    print('-' * 20)  

print("Goodbye!")
