import sqlite3
from datetime import datetime

import psycopg2
from psycopg2 import sql
from psycopg2.extras import DictCursor


class TestGenre:
    def test_row_count(sqlite_curs, pg_curs, table_name):
        """Количестов строк таблиц идентично"""
        sqlite_curs = sqlite_conn.cursor()
        sqlite_curs.execute("SELECT COUNT (id) FROM '%s';" % table_name)
        sqlite_row_count = sqlite_curs.fetchone()
        sqlite_curs.close()

        pg_curs = pg_conn.cursor()
        pg_curs.execute(
            sql.SQL("SELECT COUNT (id) FROM {table}").format(
                table=sql.Identifier(table_name)))
        pg_row_count = pg_curs.fetchone()
        pg_curs.close()

        assert sqlite_row_count[0] == pg_row_count[0]

    def test_row_consistency(sqlite_curs, pg_curs, table_name):
        """Содержание строк таблиц идентично"""
        sqlite_curs = sqlite_conn.cursor()
        sqlite_curs.execute("SELECT * FROM '%s';" % table_name)
        sqlite_rows = list(sqlite_curs.fetchall())
        result = []

        for row in sqlite_rows:
            row = list(row)
            row[3] = datetime.strptime(
                row[3] + ':00', '%Y-%m-%d %H:%M:%S.%f%z')
            row[4] = datetime.strptime(
                row[4] + ':00', '%Y-%m-%d %H:%M:%S.%f%z')
            result.append(row)
        sqlite_rows = result
        sqlite_curs.close()

        pg_curs = pg_conn.cursor()
        pg_curs.execute(
            sql.SQL("SELECT * FROM {table}").format(table=sql.Identifier(table_name)))
        pg_rows = pg_curs.fetchall()
        pg_curs.close()
        assert sqlite_rows == pg_rows
        print("Содержание строк таблиц genre идентично")


class TestPerson:
    def test_row_count(sqlite_curs, pg_curs, table_name):
        """Количестов строк таблиц идентично"""
        sqlite_curs = sqlite_conn.cursor()
        sqlite_curs.execute("SELECT COUNT (id) FROM '%s';" % table_name)
        sqlite_row_count = sqlite_curs.fetchone()
        sqlite_curs.close()

        pg_curs = pg_conn.cursor()
        pg_curs.execute(
            sql.SQL("SELECT COUNT (id) FROM {table}").format(
                table=sql.Identifier(table_name)))
        pg_row_count = pg_curs.fetchone()
        pg_curs.close()

        assert sqlite_row_count[0] == pg_row_count[0]

    def test_row_consistency(sqlite_curs, pg_curs, table_name):
        """Содержание строк таблиц идентично"""
        sqlite_curs = sqlite_conn.cursor()
        sqlite_curs.execute(
            "SELECT id, full_name, created_at, updated_at FROM '%s' ORDER BY id;" %
            table_name)
        sqlite_rows = list(sqlite_curs.fetchall())
        result = []

        for row in sqlite_rows:
            row = list(row)
            row[2] = datetime.strptime(
                row[2] + ':00', '%Y-%m-%d %H:%M:%S.%f%z')
            row[3] = datetime.strptime(
                row[3] + ':00', '%Y-%m-%d %H:%M:%S.%f%z')
            result.append(row)
        sqlite_rows = result
        sqlite_curs.close()

        pg_curs = pg_conn.cursor()
        pg_curs.execute(
            sql.SQL("SELECT id, full_name, created, modified FROM {table} ORDER BY id").format(
                table=sql.Identifier(table_name)))
        pg_rows = pg_curs.fetchall()
        pg_curs.close()
        assert sqlite_rows == pg_rows
        print("Содержание строк таблиц person идентично")


class TestFilmwork:
    def test_row_count(sqlite_curs, pg_curs, table_name):
        """Количестов строк таблиц идентично"""
        sqlite_curs = sqlite_conn.cursor()
        sqlite_curs.execute("SELECT COUNT (id) FROM '%s';" % table_name)
        sqlite_row_count = sqlite_curs.fetchone()
        sqlite_curs.close()

        pg_curs = pg_conn.cursor()
        pg_curs.execute(
            sql.SQL("SELECT COUNT (id) FROM {table}").format(
                table=sql.Identifier(table_name)))
        pg_row_count = pg_curs.fetchone()
        pg_curs.close()

        assert sqlite_row_count[0] == pg_row_count[0]

    def test_row_consistency(sqlite_curs, pg_curs, table_name):
        """Содержание строк таблиц идентично"""
        sqlite_curs = sqlite_conn.cursor()
        sqlite_curs.execute(
            "SELECT id, title, description, creation_date, file_path, rating, type, created_at, updated_at  FROM '%s' ORDER BY id;" %
            table_name)
        sqlite_rows = list(sqlite_curs.fetchall())
        result = []

        for row in sqlite_rows:
            row = list(row)
            row[-1] = datetime.strptime(row[-1] +
                                        ':00', '%Y-%m-%d %H:%M:%S.%f%z')
            row[-2] = datetime.strptime(row[-2] +
                                        ':00', '%Y-%m-%d %H:%M:%S.%f%z')
            result.append(row)
        sqlite_rows = result
        sqlite_curs.close()

        pg_curs = pg_conn.cursor()
        pg_curs.execute(
            sql.SQL("SELECT id, title, description, creation_date, file_path, rating, type, created, modified FROM {table} ORDER BY id").format(
                table=sql.Identifier(table_name)))
        pg_rows = pg_curs.fetchall()
        pg_curs.close()
        assert sqlite_rows == pg_rows
        print("Содержание строк таблиц filmwork идентично")


class TestGenreFilmWork:
    def test_row_count(sqlite_curs, pg_curs, table_name):
        """Количестов строк таблиц идентично"""
        sqlite_curs = sqlite_conn.cursor()
        sqlite_curs.execute("SELECT COUNT (id) FROM '%s';" % table_name)
        sqlite_row_count = sqlite_curs.fetchone()
        sqlite_curs.close()

        pg_curs = pg_conn.cursor()
        pg_curs.execute(
            sql.SQL("SELECT COUNT (id) FROM {table}").format(
                table=sql.Identifier(table_name)))
        pg_row_count = pg_curs.fetchone()
        pg_curs.close()

        assert sqlite_row_count[0] == pg_row_count[0]

    def test_row_consistency(sqlite_curs, pg_curs, table_name):
        """Содержание строк таблиц идентично"""
        sqlite_curs = sqlite_conn.cursor()
        sqlite_curs.execute(
            "SELECT id, genre_id, film_work_id, created_at FROM '%s';" %
            table_name)
        sqlite_rows = list(sqlite_curs.fetchall())
        result = []

        for row in sqlite_rows:
            row = list(row)
            row[3] = datetime.strptime(
                row[3] + ':00', '%Y-%m-%d %H:%M:%S.%f%z')
            result.append(row)
        sqlite_rows = result
        sqlite_curs.close()

        pg_curs = pg_conn.cursor()
        pg_curs.execute(
            sql.SQL("SELECT id, genre_id, film_work_id, created FROM {table}").format(
                table=sql.Identifier(table_name)))
        pg_rows = pg_curs.fetchall()
        pg_curs.close()
        assert sqlite_rows == pg_rows
        print("Содержание строк таблиц genre_film_work идентично")


class TestPersonFilmWork:
    def test_row_count(sqlite_curs, pg_curs, table_name):
        """Количестов строк таблиц идентично"""
        sqlite_curs = sqlite_conn.cursor()
        sqlite_curs.execute("SELECT COUNT (id) FROM '%s';" % table_name)
        sqlite_row_count = sqlite_curs.fetchone()
        sqlite_curs.close()

        pg_curs = pg_conn.cursor()
        pg_curs.execute(
            sql.SQL("SELECT COUNT (id) FROM {table}").format(
                table=sql.Identifier(table_name)))
        pg_row_count = pg_curs.fetchone()
        pg_curs.close()

        assert sqlite_row_count[0] == pg_row_count[0]

    def test_row_consistency(sqlite_curs, pg_curs, table_name):
        """Содержание строк таблиц идентично"""
        sqlite_curs = sqlite_conn.cursor()
        sqlite_curs.execute(
            "SELECT id, film_work_id, person_id, role, created_at FROM '%s';" %
            table_name)
        sqlite_rows = list(sqlite_curs.fetchall())
        result = []

        for row in sqlite_rows:
            row = list(row)
            row[-1] = datetime.strptime(row[-1] +
                                        ':00', '%Y-%m-%d %H:%M:%S.%f%z')
            result.append(row)
        sqlite_rows = result
        sqlite_curs.close()

        pg_curs = pg_conn.cursor()
        pg_curs.execute(
            sql.SQL("SELECT id, film_work_id, person_id, role, created FROM {table}").format(
                table=sql.Identifier(table_name)))
        pg_rows = pg_curs.fetchall()
        pg_curs.close()
        assert sqlite_rows == pg_rows
        print("Содержание строк таблиц person_film_work идентично")


SQLITE_FILE = '../../db.sqlite'
dsl = {
    'dbname': 'movies_database',
    'user': 'app',
    'password': '123qwe',
    'host': '127.0.0.1',
    'port': 5432}
with sqlite3.connect(SQLITE_FILE) as sqlite_conn, psycopg2.connect(**dsl, cursor_factory=DictCursor) as pg_conn:

    TestGenre.test_row_count(sqlite_conn, pg_conn, 'genre')
    TestGenre.test_row_consistency(sqlite_conn, pg_conn, 'genre')

    TestPerson.test_row_count(sqlite_conn, pg_conn, 'person')
    TestPerson.test_row_consistency(sqlite_conn, pg_conn, 'person')

    TestFilmwork.test_row_count(sqlite_conn, pg_conn, 'film_work')
    TestFilmwork.test_row_consistency(sqlite_conn, pg_conn, 'film_work')

    TestGenreFilmWork.test_row_count(sqlite_conn, pg_conn, 'genre_film_work')
    TestGenreFilmWork.test_row_consistency(
        sqlite_conn, pg_conn, 'genre_film_work')

    TestPersonFilmWork.test_row_count(sqlite_conn, pg_conn, 'person_film_work')
    TestPersonFilmWork.test_row_consistency(
        sqlite_conn, pg_conn, 'person_film_work')

sqlite_conn.close()
pg_conn.close()
