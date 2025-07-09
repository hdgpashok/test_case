import uvicorn
from fastapi import FastAPI


app = FastAPI()

@app.post('/reviews')
def put_comment():
    ...
    return {
        'id': 'id',
        'text': 'text',
        'sentiment': 'sentiment',
        'created_at': 'created_at'
    }


@app.get('/reviews?sentiment=negative')
def get_negative_comments():
    