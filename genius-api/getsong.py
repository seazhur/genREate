import requests  # allows you to send HTTP requests
import time

from pprint import pprint

SPOTIFY_GET_CURRENT_TRACK_URL = "https://api.spotify.com/v1/me/player/currently-playing"
SPOTIFY_ACCESS_TOKEN = "BQDU4X0fsRhqBt36qVQc2efkQvlV7Yzcehiw-G_ML04OPfvGLAvmtC9wZM0O3t7mKKkVLtd8tzYUait9bACgrg1eBqr6j1WlTsiQYZh43Ud8YuF-Y1HRPAzE1X43xl1fL1WtbCR_Kv83QdJ58gE9Pd2sIcmSJvh3iW_0MlfsECo"

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

    current_track_info = {
        "id": track_id,
        "track_name": track_name,
        "artists": artist_names,
        "link": link,
    }

    return current_track_info


def main():
    while True:
        current_track_info = get_current_track(SPOTIFY_ACCESS_TOKEN)
        pprint(
            current_track_info,
            indent=4,
        )
        time.sleep(2)


# tells python where to start program
if __name__ == "__main__":
    main()
