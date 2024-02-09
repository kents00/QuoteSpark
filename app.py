from flask import Flask, render_template, request

app = Flask(__name__)

# Sample data - Quotes with associated keywords and authors
quotes_data = [
    {"quote": "Happiness is not something ready made. It comes from your own actions.",
        "author": "Dalai Lama", "keywords": ["happy"]},
    {"quote": "The only way to do great work is to love what you do.",
        "author": "Steve Jobs", "keywords": ["happy", "motivation"]},
    {"quote": "The best way to cheer yourself is to try to cheer someone else up.",
        "author": "Mark Twain", "keywords": ["happy", "kindness"]},
    {"quote": "The only thing we have to fear is fear itself.",
        "author": "Franklin D. Roosevelt", "keywords": ["fear"]},
    {"quote": "Sadness flies away on the wings of time.",
        "author": "Jean de La Fontaine", "keywords": ["sad"]},
    # Add more quotes here
]


@app.route('/')
def index():
    unique_keywords = set()
    for quote in quotes_data:
        unique_keywords.update(quote['keywords'])
    return render_template('index.html', quotes=quotes_data, keywords=unique_keywords)


@app.route('/keyword/<keyword>')
def keyword_quotes(keyword):
    filtered_quotes = [
        quote for quote in quotes_data if keyword in quote['keywords']]
    return render_template('keyword_quotes.html', keyword=keyword, quotes=filtered_quotes)


@app.route('/author/<author>')
def author_quotes(author):
    filtered_quotes = [
        quote for quote in quotes_data if author.lower() == quote['author'].lower()]
    return render_template('author_quotes.html', author=author, quotes=filtered_quotes)


if __name__ == '__main__':
    app.run(debug=True)
