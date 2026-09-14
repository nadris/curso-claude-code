import os


def get_connection():
    import psycopg2

    return psycopg2.connect(os.environ["DATABASE_URL"])


def save_note(conn, text: str) -> None:
    normalized = text.strip()
    if not normalized:
        raise ValueError("text no puede estar vacío")

    with conn.cursor() as cur:
        cur.execute("INSERT INTO notes (text) VALUES (%s)", (normalized,))
    conn.commit()


def fetch_notes(conn) -> list[str]:
    with conn.cursor() as cur:
        cur.execute("SELECT text FROM notes ORDER BY id")
        return [row[0] for row in cur.fetchall()]
