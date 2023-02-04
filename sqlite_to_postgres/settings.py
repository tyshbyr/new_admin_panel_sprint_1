import os

from dotenv import load_dotenv
from script import TableColumns

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SQLITE_FILE = os.path.join(BASE_DIR, os.environ.get('SQLITE_FILE'))
SQLITE_TABLE = TableColumns(
    os.environ.get('SQLITE_TABLE'),
    os.environ.get('SQLITE_COLUMNS'))
LIMIT = int(os.environ.get('LIMIT'))

PG_TABLE = TableColumns(
    os.environ.get('PG_TABLE'),
    os.environ.get('PG_COLUMNS'))
