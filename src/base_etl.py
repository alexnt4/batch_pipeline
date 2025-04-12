from cfg import CLIENT_ID, CLIENT_SECRET, SPOTIPY_REDIRECT_URL, DB_CONNSTR
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime, timedelta

import pandas as pd
from sqlalchemy import create_engine


scope = "user-read_recently-played"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URL,
                                               scope=scope))


def extract(date, limit=50):
    """Get limit elements form last listen tracks

    Args:
       ds (datetime): Date to query
       limit (int): Limit of elements to query
    """
    
    ds = int(date.timestamp()) * 1000
    return sp.current_user_recently_played(limit=limit, after=ds)


if __name__ == "__main__":
    date = datetime.today() - timedelta(days=1)

    # Extract
    data_raw = extract(date)
    print("Extracted {(data_raw['items'])} registers")
    breakpoint()
