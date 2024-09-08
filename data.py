from dataclasses import dataclass
import discogs_client
import csv
import json

PATH = "/Users/josh/albumdle-data/albums.json"

# import the directory of albums
albums = []
with open('albums.csv', mode='r')as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        albums.insert(len(albums), lines)
albums.pop(0)


# set up api token and connect to client
token = 'ipACfctfqlQiRApGndTeBACoWkVlqsrIalJnZnKD'

d = discogs_client.Client(
    'manlikejosh/0.1', user_token=token)


@dataclass
class Album:
    title: str
    artist: list
    ratings: str
    year: str
    genres: list
    style: list
    tracklist: str


# iniate the holder array
to_json = []

# begin to parse through each album an place into json file
for album in albums:
    this_album = []
    first_search = d.search(album[0], artist=album[1], type='release')
    if first_search.pages > 0:
        if len(first_search) > 0:
            this_id = first_search[0].id
            search_album = d.release(this_id)

            this_album.append(search_album.title)
            this_album.append(search_album.artists[0].name)
            this_album.append(search_album.community.rating.average)
            this_album.append(search_album.year)
            this_album.append(search_album.genres)
            this_album.append(search_album.styles)
            num_tracks = search_album.tracklist
            this_album.append(len(num_tracks))

            to_json.append(Album(*this_album).__dict__)

            with open(PATH, "w") as file:
                json.dump(to_json, file, indent=4)

            print(len(to_json), search_album.title, " is done ")
            quit
        else:
            print("No results found.")

    else:
        print("No results found.")

# with open(PATH, "w") as file:
#     json.dump(to_json, file, indent=4)
