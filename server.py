import os
import psycopg2
from flask import Flask, render_template
from dotenv import load_dotenv
app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='lab-render-pedroaraujo4910-1b67.e.aivencloud.com',
                            database='movies',
                            user=os.getenv("DB_USERNAME"),
                            password=os.getenv("DB_PASSWORD"),
                            port='21261')
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM movies;')
    movies = [] 
    moviesFet = cur.fetchall()
    cur.close()
    conn.close()
    
    """
    HTML (<li>) de todos os dados.
    """
    html = ""
    
    for row in moviesFet:
        movies.append({"name": row[0], "rating": row[1]})
    
    for movie in movies:
    
        html = html + """
            <li class="list-group-item">
                <span class="badge">%s
                    <span class="glyphicon glyphicon-star"></span>
                </span>
                %s
            </li>
        """ % (movie['rating'], movie['name'])
       
    return open('index.html').read()  % (html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)