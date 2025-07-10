# test_case
pip install fastapi uvicorn
uvicorn main:app --reload

curl -X 'POST' \
  'http://127.0.0.1:8000/reviews' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "какой-то текст ненавиж"
}'

responce: 
{
  "id": 9,
  "text": "какой-то текст ненавиж",
  "sentiment": "negative",
  "created_at": "2025-07-10T00:28:49.169252"
}

curl -X 'GET' \
  'http://127.0.0.1:8000/reviews/sentiment=negative' \
  -H 'accept: application/json'
responce:
[
  {
    "id": 6,
    "text": "sdfsdfsdf плохо",
    "sentiment": "negative",
    "created_at": "2025-07-10T00:11:15.392452"
  },
  {
    "id": 7,
    "text": "sdfsdfsdf плохо",
    "sentiment": "negative",
    "created_at": "2025-07-10T00:12:04.784584"
  },
  {
    "id": 8,
    "text": "qwery ненавиж",
    "sentiment": "negative",
    "created_at": "2025-07-10T00:20:11.037895"
  },
  {
    "id": 9,
    "text": "какой-то текст ненавиж",
    "sentiment": "negative",
    "created_at": "2025-07-10T00:28:49.169252"
  }
]
