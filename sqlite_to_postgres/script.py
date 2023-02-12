import io
import sqlite3
from contextlib import contextmanager
from dataclasses import dataclass, field

from psycopg2.extensions import connection as _connection


@contextmanager
def conn_context(db_path: str):
    conn = sqlite3.connect(f"file:{db_path}?mode=rw", uri=True)
    yield conn
    conn.close()


class SQLiteExtractor:
    def __init__(self, conn: sqlite3.Connection,
                 limit: int, 
                 class_table: tuple) -> None:
        self.conn = conn
        self.class_table = class_table
        self.limit = limit

    def extract_movies(self):
        for cls, table in self.class_table:
            self.conn.row_factory = cls.row_factory
            curs = self.conn.cursor()
            curs.arraysize = self.limit
            curs.execute(f"SELECT * FROM {table};")
            while True:
                data = curs.fetchmany()
                if not data:
                    break
                yield table, data


@dataclass
class PostgresSaver:
    def __init__(self, pg_conn: _connection) -> None:
        self.pg_conn = pg_conn

    def save_all_data(self, data) -> None:       
        with self.pg_conn.cursor() as curs:
            for table, rows in data:
                columns = rows[0].to_pg().keys()
                print(table, columns)
                value = '\n'.join(['\t'.join(item for item in row.to_pg().values()) for row in rows])
                data_file = io.StringIO()
                data_file.write(value)
                data_file.seek(0)
                curs.copy_from(
                    data_file,
                    table,
                    sep='\t',
                    null='None',
                    columns=columns)
