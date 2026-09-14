import pytest

from app.persistence import fetch_notes, get_connection, save_note


@pytest.fixture
def conn():
    connection = get_connection()
    with connection.cursor() as cur:
        cur.execute(
            "CREATE TABLE IF NOT EXISTS notes (id SERIAL PRIMARY KEY, text TEXT NOT NULL)"
        )
        cur.execute("TRUNCATE notes RESTART IDENTITY")
    connection.commit()
    yield connection
    connection.close()


def test_save_and_fetch_notes_against_real_postgres(conn):
    save_note(conn, "hola")

    assert fetch_notes(conn) == ["hola"]
