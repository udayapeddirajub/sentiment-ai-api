from flask import Flask, request, jsonify, render_template
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get('text', '')
    analysis = TextBlob(text)
    
    polarity = analysis.sentiment.polarity
    sentiment = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
    
    return jsonify({
        "sentiment": sentiment,
        "score": round(polarity, 2)
    })

if __name__ == '__main__':
    app.run(debug=True)
