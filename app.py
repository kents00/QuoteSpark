from flask import Flask, render_template, jsonify
from flask_restful import Api, Resource
import sqlite3
import random

app = Flask(__name__)
api = Api(app)

def get_quotes_from_db():
    conn = sqlite3.connect('quotes.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM quotes")
    quotes = cursor.fetchall()
    conn.close()
    return [{'quote': quote[1], 'author': quote[2]} for quote in quotes]

@app.route('/')
def index():
    quotes_data = get_quotes_from_db()
    random_quote = random.choice(quotes_data)
    return render_template('index.html', quotes=quotes_data, random_quote=random_quote)


@app.route('/author/<author>')
def author_quotes(author):
    quotes_data = get_quotes_from_db()
    filtered_quotes = [
        quote for quote in quotes_data if author.lower() == quote['author'].lower()]
    return render_template('author_quotes.html', author=author, quotes=filtered_quotes)

# API routes remain unchanged


class QuoteList(Resource):
    def get(self):
        quotes_data = get_quotes_from_db()
        return jsonify(quotes_data)


class RandomQuote(Resource):
    def get(self):
        quotes_data = get_quotes_from_db()
        quote = random.choice(quotes_data)
        return jsonify(quote)


class KeywordQuotes(Resource):
    def get(self, keyword):
        quotes_data = get_quotes_from_db()
        filtered_quotes = [
            quote for quote in quotes_data if keyword in quote['quote']]
        return jsonify(filtered_quotes)


class AuthorQuotes(Resource):
    def get(self, author):
        quotes_data = get_quotes_from_db()
        filtered_quotes = [
            quote for quote in quotes_data if author.lower() == quote['author'].lower()]
        return jsonify(filtered_quotes)


api.add_resource(QuoteList, '/api/quotes')
api.add_resource(RandomQuote, '/api/random')
api.add_resource(KeywordQuotes, '/api/keyword/<string:keyword>')
api.add_resource(AuthorQuotes, '/api/author/<string:author>')

if __name__ == '__main__':
    app.run(debug=True)
