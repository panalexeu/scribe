import os

from starlette.config import Config
from authlib.integrations.starlette_client import OAuth

config_data = {
    'GOOGLE_CLIENT_ID': os.environ.get('GOOGLE_CLIENT_ID'),
    'GOOGLE_CLIENT_SECRET': os.environ.get('GOOGLE_CLIENT_SECRET')
}


def setup_google_oauth() -> OAuth:
    print(os.environ.get('GOOGLE_CLIENT_ID'), os.environ.get('GOOGLE_CLIENT_SECRET'))
    oauth = OAuth(config=Config(environ=config_data))
    oauth.register(
        name='google',
        server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
        client_kwargs={'scope': 'openid email profile'},
    )

    return oauth

