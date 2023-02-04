import io
import sqlite3
from contextlib import contextmanager
from dataclasses import dataclass, field

from psycopg2.extensions import connection as _connection


@dataclass
class TableColumns:
    table: str
    columns: str


@contextmanager
def conn_context(db_path: str):
    conn = sqlite3.connect(f"file:{db_path}?mode=rw", uri=True)
    yield conn
    conn.close()


@dataclass
class SQLiteExtractor:
    conn: sqlite3.Connection
    sqlite_table: TableColumns
    limit: int = field(default=100)

    def extract_movies(self):
        curs = self.conn.cursor()
        curs.arraysize = self.limit
        curs.execute(
            f"SELECT {self.sqlite_table.columns} FROM {self.sqlite_table.table};")
        while True:
            data = curs.fetchmany()
            if not data:
                break
            yield data


@dataclass
class PostgresSaver:
    pg_conn: _connection
    pg_table: TableColumns

    def save_all_data(self, data):
        with self.pg_conn.cursor() as curs:
            columns = self.pg_table.columns.split(',')
            placeholder = '\t'.join('%s' for _ in range(len(columns)))

            for value in data:
                print(value)
                args = ''.join(f'{placeholder}\n' % item for item in value)
                print(args)
                data_file = io.StringIO()
                data_file.write(args)
                data_file.seek(0)
                curs.copy_from(
                    data_file,
                    self.pg_table.table,
                    sep='\t',
                    null='None',
                    columns=columns)
