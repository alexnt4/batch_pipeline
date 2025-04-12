from decouple import Config, RepositoryIni

# Especifica la ruta a tu archivo .ini
config = Config(RepositoryIni("settings.ini"))

CLIENT_ID = config("CLIENT_ID")
CLIENT_SECRET = config("CLIENTE_SECRET")
SPOTIPY_REDIRECT_URL = config("SPOTIPY_REDIRECT_URI")
DB_CONNSTR = config("DB_CONNSTR")
