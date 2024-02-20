from flask import Flask, render_template, jsonify, request
from flask_restful import Api, Resource
from flask_caching import Cache
import sqlite3
import random

config = {
    "DEBUG": True,
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 300
}

app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)
api = Api(app)

def get_quotes_from_db():
    conn = sqlite3.connect('quotes.db')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT quote, author FROM quotes")
    quotes = cursor.fetchall()
    conn.close()
    return [{'quote': quote[0], 'author': quote[1]} for quote in quotes]


def get_authors_from_db():
    conn = sqlite3.connect('quotes.db')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT author FROM quotes")
    authors = cursor.fetchall()
    conn.close()
    return [author[0] for author in authors]


@app.route('/')
@cache.cached(timeout=10)
def index():
    quotes_data = get_quotes_from_db()
    random_quote = random.choice(quotes_data)
    return render_template('homepage.html', quotes=quotes_data, random_quote=random_quote)

@app.route("/robots.txt")
def robots_dot_txt():
    return "User-agent: *\nAllow: /"

@app.route('/authors/<author>')
@cache.cached(timeout=300)
def author_quotes(author):
    quotes_data = get_quotes_from_db()
    filtered_quotes = [
        quote for quote in quotes_data if author.lower() == quote['author'].lower()]
    return render_template('author_quotes.html', author=author, quotes=filtered_quotes)


@app.route('/authors')
def author_list():
    page = request.args.get('page', 1, type=int)
    per_page = 30  # Number of authors per page
    all_authors = get_authors_from_db()
    total_pages = (len(all_authors) + per_page - 1) // per_page
    start_index = (page - 1) * per_page
    end_index = start_index + per_page
    paginated_authors = all_authors[start_index:end_index]
    return render_template('author_list.html', authors=paginated_authors, page=page, total_pages=total_pages)


class QuoteList(Resource):
    @cache.cached(timeout=300)
    def get(self):
        quotes_data = get_quotes_from_db()
        return jsonify(quotes_data)


class RandomQuote(Resource):
    @cache.cached(timeout=5)
    def get(self):
        quotes_data = get_quotes_from_db()
        quote = random.choice(quotes_data)
        return jsonify(quote)


class AuthorQuotes(Resource):
    @cache.cached(timeout=5)
    def get(self, author):
        quotes_data = get_quotes_from_db()
        filtered_quotes = [
            quote for quote in quotes_data if author.lower() == quote['author'].lower()]
        return jsonify(filtered_quotes)


api.add_resource(QuoteList, '/api/quotes')
api.add_resource(RandomQuote, '/api/random')
api.add_resource(AuthorQuotes, '/api/author/<string:author>')

if __name__ == '__main__':
    app.run(debug=True)
