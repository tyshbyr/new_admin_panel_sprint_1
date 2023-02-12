import sqlite3

import psycopg2
import settings
from psycopg2.extensions import connection as _connection
from psycopg2.extras import DictCursor
from script import PostgresSaver, SQLiteExtractor, conn_context


def load_from_sqlite(connection: sqlite3.Connection, pg_conn: _connection, batch_size: int, class_table: tuple):
    """Основной метод загрузки данных из SQLite в Postgres"""
    postgres_saver = PostgresSaver(pg_conn)
    sqlite_extractor = SQLiteExtractor(
        connection, batch_size, class_table)

    data = sqlite_extractor.extract_movies()
    postgres_saver.save_all_data(data)


if __name__ == '__main__':
    dsl = {
        'dbname': 'movies_database',
        'user': 'app',
        'password': '123qwe',
        'host': '127.0.0.1',
        'port': 5432}
    with conn_context(settings.SQLITE_FILE) as sqlite_conn, psycopg2.connect(**dsl, cursor_factory=DictCursor) as pg_conn:
        load_from_sqlite(sqlite_conn, pg_conn, settings.BATCH_SIZE, settings.CLASS_TABLE_TUPLE)
