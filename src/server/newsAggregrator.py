from flask import Flask, jsonify, request
from pymongo import MongoClient
import requests
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

CORS(app)
client = MongoClient('mongodb://localhost:27017/newsdb')

db = client.newsdb
news_collection = db.news

@app.route('/api/news', methods=['GET'])

def fetch_news():
    try:
        url = ('https://newsapi.org/v2/top-headlines?'
       'sources=bbc-news&'
       'apiKey=eec8a8b945874740b494317298c49a5e')
        params = {
            'pageSize': 10,
            'sortBy': 'popularity',
            
        }
        response = requests.get(url,params=params)
        response.raise_for_status()
        data = response.json()
        if 'articles' in data:
            articles = data.get('articles',[])
            return[{
                'source': article['source']['name'],
                'author': article['author'],
                'title': article['title'],
                'description': article['description'],
                'url': article['url'],
                'urlToImage': article['urlToImage'],
                'publishedAt': article['publishedAt'],
                'content': article['content']
            } for article in articles]
        
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500
    

def get_news():
    try:
        news = list(news_collection.find({}, {'_id': 0}))
        return jsonify(news), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500
    
# Route to update news by fetching from the News API
@app.route('/api/news/update', methods=['POST'])

def update_news():
    try:
        articles = fetch_news()
        news_collection.delete_many({})
        news_collection.insert_many(articles)
        return jsonify({'message': 'News updated successfully'}), 200
    
    except Exception as e:
        return jsonify({'message': str(e)}), 500
    
    
@app.route('/')
def index():
    return "News Aggregator API"

if __name__ == '__main__':
    app.run(debug=True)

