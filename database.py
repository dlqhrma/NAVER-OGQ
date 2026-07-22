import sqlite3

DB_NAME = "cbt.db"

def get_connection():
    return sqlite3.connect(DB_NAME)


def save_exam(exam_date, score, total_questions, duration):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO exams
        (exam_date, score, total_questions, duration)
        VALUES (?, ?, ?, ?)
    """, (exam_date, score, total_questions, duration))

    exam_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return exam_id