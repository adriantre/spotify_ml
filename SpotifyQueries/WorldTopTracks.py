import spotipy
import spotipy.util as util
import pandas as pd
import os

def parseTrack(item):
    track = {}
    track['album'] = item['album']['name']
    track['artist'] = item['artists'][0]['name']
    track['duration_ms'] = item['duration_ms']
    track['track_id'] = item['id']
    track['track_name'] = item['name']
    track['popularity'] = item['popularity']
    track['track_uri'] = item ['uri']
    return track

def queryWorldTopTracks():   
    scope = 'user-top-read'
    USERNAME = os.environ['USERNAME']
    SPOTIPY_CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
    SPOTIPY_CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']
    SPOTIPY_REDIRECT_URI = os.environ['SPOTIPY_REDIRECT_URI']
    token = util.prompt_for_user_token(
        USERNAME,
        scope,
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI
    )
    sp = spotipy.Spotify(auth=token)
    columns = ['album','artist','duration_ms','track_id','track_name','popularity','track_uri']
    
    dislike_df = pd.read_csv("world_top_135_raw.csv")
    dislike_df['track_uri'] = dislike_df['Track URL']
    dislike_df = dislike_df.reindex(columns = ['track_uri'])
    dislike_df[columns] = dislike_df.apply(
        (lambda track: pd.Series(parseTrack(sp.track(track['track_uri']))))
        , axis=1, result_type="expand")
    track_feature_cols = ['danceability','energy','key','loudness','mode','speechiness',
        'acousticness','instrumentalness','liveness','valence','tempo','type','id','uri',
        'track_href','analysis_url','duration_ms','time_signature']
    dislike_df[track_feature_cols] = dislike_df.apply(
        (lambda track: pd.Series(sp.audio_features(track['track_uri'])[0]))
        , axis=1, result_type="expand")
    return dislike_df