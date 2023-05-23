# make a function to collect information in directory
def make_album(artist_name, album_title, songs_in_album = None, listening = None,):
    '''Make album info'''
    album = {"name": artist_name, "title": album_title,}
    if songs_in_album:
        album["songs in album"] = songs_in_album
    if listening:
        album["play times"] = listening
    return album

first_album = make_album("50 CENT", "Get Ritch or die try", 34 )
print(first_album)
# ask to user enter information
while True:
    print("\n\tEnter information about the album: ")
    print("\t\t(enter 'q' to exit)")

    a_name = input("Artist Name: ")
    if a_name == "q":
        break

    a_title = input("Album Title: ")
    if a_title == "q":
        break

    song_count = input("How many songs are in the album: ")
    song_coint = int(song_count)
    if song_count == "q":
        break

    listening_count = input("Times it been played: ")
    listening_count = int(listening_count)
    if listening_count == "q":
        break

    album_info = make_album(a_name, a_title, song_coint, listening_count)
    print(album_info)

all_albums = []
all_albums.append(album_info)

print(all_albums)
    