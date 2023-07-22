import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set your Spotify app credentials and scopes
client_id = 'eaec677f2e8945338b3d54ca64b82218'
client_secret = '4dbcd121816c486e86b508c9d9586e7b'
redirect_uri = 'https:/localhost:8888/callback'
username = 'Ajay Kataria'
scope = "user-library-read,playlist-read-private"

# Initialize Spotify client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope,
                                               username=username))

# Open the output file
with open('output.txt', 'w',encoding='utf-8') as f:

    # Get liked songs
    results = sp.current_user_saved_tracks()
    for idx, item in enumerate(results['items']):
        track = item['track']
        f.write(f"{idx}: {track['artists'][0]['name']} – {track['name']}\n")

    # Get songs from playlists
    playlists = sp.current_user_playlists()['items']
    for playlist in playlists:
        f.write(f"\nPlaylist: {playlist['name']}\n{'-' * len(playlist['name'])}\n")
        results = sp.playlist(playlist['id'], fields="tracks,next")
        tracks = results['tracks']
        for i, item in enumerate(tracks["items"]):
            track = item['track']
            f.write(f"{i}: {track['artists'][0]['name']} – {track['name']}\n")
