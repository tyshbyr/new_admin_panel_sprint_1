import os

from dotenv import load_dotenv

from dataclass import Genre, Person, Filmwork, PersonFilmwork, GenreFilmwork

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SQLITE_FILE = os.path.join(BASE_DIR, os.environ.get('SQLITE_FILE'))

BATCH_SIZE = int(os.environ.get('LIMIT'))



CLASS_TABLE_TUPLE = (
    (Genre, 'genre'), 
    (Person, 'person'), 
    (Filmwork, 'film_work'), 
    (PersonFilmwork, 'person_film_work'), 
    (GenreFilmwork, 'genre_film_work'))
