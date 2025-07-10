from datetime import datetime
import sqlite3

from fastapi import FastAPI
from pydantic import BaseModel


def init_db():
    connection = sqlite3.connect('reviews.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reviews (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      text TEXT NOT NULL,
      sentiment TEXT NOT NULL,
      created_at TEXT NOT NULL
    )
    ''')


init_db()
app = FastAPI()

sentiment_words = {
    'positive': ['хорош', 'люблю'],
    'negative': ['плохо', 'ненавиж']
}


class CommentSchema(BaseModel):
    text: str


class PostCommentSchema(BaseModel):
    id: int
    text: str
    sentiment: str
    created_at: str


def get_sentiment(text: str):
    text = text.lower()
    for sentiment, words in sentiment_words.items():
        if any(word in text for word in words):
            return sentiment
    return 'neutral'


@app.post('/reviews')
def create_comment(comment: CommentSchema):
    sentiment = get_sentiment(comment.text)
    created_at = datetime.utcnow().isoformat()
    connection = sqlite3.connect('reviews.db')
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO reviews (text, sentiment, created_at) VALUES (?, ?, ?)
    """,
                   (comment.text, sentiment, created_at)
                   )
    connection.commit()
    responce_id = cursor.lastrowid
    return {
        'id': responce_id,
        'text': comment.text,
        'sentiment': sentiment,
        'created_at': created_at
    }


@app.get('/reviews/sentiment=negative')
def get_negative_comments():
    connection = sqlite3.connect('reviews.db')
    cursor = connection.cursor()
    cursor.execute("""
    SELECT * FROM reviews WHERE sentiment = 'negative'
    """)
    connection.commit()
    return [
        {
            'id': row[0],
            'text': row[1],
            'sentiment': row[2],
            'created_at': row[3]
        }
        for row in cursor.fetchall()
    ]
