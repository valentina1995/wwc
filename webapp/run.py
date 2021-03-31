from flask import render_template
from flask_cors import cross_origin
from app import create_app
from config import Config

app = create_app(Config)

@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run() 