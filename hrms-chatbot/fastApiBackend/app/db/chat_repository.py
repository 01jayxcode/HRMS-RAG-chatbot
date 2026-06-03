from app.db.database import get_connection
import uuid

def create_session(user_id: str = None) -> str:
    session_id = str(uuid.uuid4())
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO chat_sessions (session_id, user_id) VALUES (%s, %s)",
        (session_id, user_id)
    )
    conn.commit()
    cur.close()
    conn.close()
    return session_id


def save_message(session_id: str, role: str, content: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO chat_messages (session_id, role, content) VALUES (%s, %s, %s)",
        (session_id, role, content)
    )
    conn.commit()
    cur.close()


def get_history(session_id: str) -> list:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT role, content FROM chat_messages WHERE session_id = %s ORDER BY created_at ASC",
        (session_id,)
    )
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [{"role": row[0], "content": row[1]} for row in rows]


def session_exists(session_id: str) -> bool:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT 1 FROM chat_sessions WHERE session_id = %s",
        (session_id,)
    )
    exists = cur.fetchone() is not None
    cur.close()
    conn.close()
    return exists