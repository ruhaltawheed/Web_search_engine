from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    query = request.args.get('q')
    results = []

    if query:
        conn = sqlite3.connect("data/documents.db")
        c = conn.cursor()
        c.execute("SELECT title, url, content FROM documents WHERE content LIKE ?", ('%' + query + '%',))
        results = c.fetchall()
        conn.close()

    return render_template('index.html', results=results, query=query)

if __name__ == '__main__':
    app.run(debug=True)