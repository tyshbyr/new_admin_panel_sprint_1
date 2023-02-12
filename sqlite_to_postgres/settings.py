import os

from dotenv import load_dotenv

from dataclass import Genre, Person, Filmwork, PersonFilmwork, GenreFilmwork


load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SQLITE_FILE = os.path.join(BASE_DIR, os.environ.get('SQLITE_FILE'))

BATCH_SIZE = int(os.environ.get('LIMIT'))

dsl = {
        'dbname': os.environ.get('DB_NAME'),
        'user': os.environ.get('DB_USER'),
        'password': os.environ.get('DB_PASSWORD'),
        'host': os.environ.get('DB_HOST'),
        'port': os.environ.get('DB_PORT')}

CLASS_TABLE = (
    (Genre, 'genre'), 
    (Person, 'person'), 
    (Filmwork, 'film_work'), 
    (PersonFilmwork, 'person_film_work'), 
    (GenreFilmwork, 'genre_film_work'))
