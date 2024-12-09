from flask import Flask, render_template
import sqlite3
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('index.html')

@app.route('/data')
def data():
    conn = sqlite3.connect('../database/data.db')
    
    df = pd.read_sql('SELECT * FROM gym_data', conn)
    
    conn.close()
    
    df_cleaned = df.applymap(lambda x: str(x).replace('\n', '').strip() if isinstance(x, str) else x)

    table_html = df_cleaned.to_html(classes='data', index=False)

    table_html = table_html.replace('\n', '')

    return render_template('data.html', tables=table_html, titles=df.columns.values)

if __name__ == '__main__':
    app.run(debug=True)
