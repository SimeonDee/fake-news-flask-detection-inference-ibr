from flask import (Flask, request, jsonify, render_template, url_for)
from utilities import predict

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    # else:
    #     data = request.json()
    #     return render_template('index.html', data=data)

@app.route('/classify-news', methods=['POST'])
def classify_news():
    if request.method == 'POST':
        data = request.json
        results = predict(news_article=data['news'], model_type=data['model'])
        return jsonify({'results': results})
    else:
        return jsonify({'results': None})


if __name__ == '__main__':
    app.run(debug=True)