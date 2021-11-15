import json
import requests  # allows you to send HTTP requests
import time

from pprint import pprint
from bs4 import BeautifulSoup

SPOTIFY_GET_CURRENT_TRACK_URL = "https://api.spotify.com/v1/me/player/currently-playing"
SPOTIFY_ACCESS_TOKEN = "BQDU4X0fsRhqBt36qVQc2efkQvlV7Yzcehiw-G_ML04OPfvGLAvmtC9wZM0O3t7mKKkVLtd8tzYUait9bACgrg1eBqr6j1WlTsiQYZh43Ud8YuF-Y1HRPAzE1X43xl1fL1WtbCR_Kv83QdJ58gE9Pd2sIcmSJvh3iW_0MlfsECo"

GENIUS_SEARCH_URL = "https://api.genius.com/search"
GENIUS_ACCESS_TOKEN = "FbC-0Tt4FZN3I7AI2U11IxR91SJRjwn1K4F3TEpoakwzpzOH-E5ZPbKAbfTxUh8F"

defaults = {
    "request": {"token": GENIUS_ACCESS_TOKEN, "base_url": "https://api.genius.com"},
    "message": {
        "search_fail": "The lyrics for this song were not found!",
    },
}

# writes lyrics to a file
def write_lyrics_to_file(lyrics, song, artist):
    f = open("lyrics.txt", "w")
    f.write("{} by {}".format(song, artist))
    f.write(lyrics)
    f.close()


# scraps genius song page for lyrics
def scrap_song_url(url):
    page = requests.get(url)
    html = BeautifulSoup(page.text, "html.parser")
    [h.extract() for h in html("script")]
    lyrics = html.find("div", class_="lyrics").get_text()
    return lyrics


# searches genius response object for song lyrics
def print_lyrics(response, song_title, artist_name):
    json = response.json()
    remote_song_info = None

    # searches for song match based on primary artist name
    for hit in json["response"]["hits"]:
        if artist_name.lower() in hit["result"]["primary_artist"]["name"].lower():
            remote_song_info = hit
            break

    # search remote song object for genius url
    if remote_song_info:
        song_url = remote_song_info["result"]["url"]
        lyrics = scrap_song_url(song_url)
        # write_lyrics_to_file(lyrics, song_title, artist_name)
        print(lyrics)
    else:
        print(defaults["message"]["search_fail"])


# sends request to genius api for song results
def request_song_info(song_title, artist_names, access_token):
    data = {"q": song_title + " " + artist_names}

    response = requests.get(
        GENIUS_SEARCH_URL,
        data,
        headers={"Authorization": f"Bearer {access_token}"},
    )

    print_lyrics(response, song_title, artist_names)


# returns song information in dictionary format
def get_current_track(access_token):
    # Send api request in spotifyapi format
    response = requests.get(
        SPOTIFY_GET_CURRENT_TRACK_URL,
        headers={"Authorization": f"Bearer {access_token}"},
    )
    # when request library is used for api call, respose object is sent back
    json_resp = response.json()

    # access json data like nested array
    track_id = json_resp["item"]["id"]
    track_name = json_resp["item"]["name"]
    # array of artist objects
    artists = [artist for artist in json_resp["item"]["artists"]]
    # join takes an array of artist names and joins each one with the ", " string
    artist_names = ", ".join([artist["name"] for artist in artists])
    link = json_resp["item"]["external_urls"]["spotify"]

    primary_artist = artists[0]["name"]

    current_track_info = {
        "id": track_id,
        "track_name": track_name,
        "artists": primary_artist,
        "link": link,
    }

    return current_track_info


def main():
    current_track_info = get_current_track(SPOTIFY_ACCESS_TOKEN)
    pprint(
        current_track_info,
        indent=4,
    )
    values = list(current_track_info.values())
    song_title = values[1]
    artist_names = values[2]

    request_song_info(song_title, artist_names, GENIUS_ACCESS_TOKEN)

    # loop version
    # while True:
    #     current_track_info = get_current_track(ACCESS_TOKEN)
    #     pprint(
    #         current_track_info,
    #         indent=4,
    #     )
    # values = list(current_track_info.values())
    # song_title = values[1]
    # artist_names = values[2]

    # request_song_info(song_title, artist_names, GENIUS_ACCESS_TOKEN)
    #     time.sleep(2)


if __name__ == "__main__":
    main()
