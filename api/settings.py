'''Main settings for backend'''

from os import getenv

from dotenv import load_dotenv


load_dotenv()


# APP
DEBUG = getenv('DEBUG', default='0').lower() in ['1', 'true']

# DATABASE
POSTGRES_HOST = getenv('POSTGRES_HOST', default='0.0.0.0')
POSTGRES_PORT = getenv('POSTGRES_PORT', default='5432')
POSTGRES_USER = getenv('POSTGRES_USER', default='postgres')
POSTGRES_PASSWORD = getenv('POSTGRES_PASSWORD', default='postgres')
POSTGRES_DATABASE = getenv('POSTGRES_DATABASE', default='postgres')
POSTGRES_URL = (
    'postgres+asyncpg://'
    f'{POSTGRES_USER}:{POSTGRES_PASSWORD}@'
    f'{POSTGRES_HOST}:{POSTGRES_PORT}/'
    f'{POSTGRES_DATABASE}'
)
