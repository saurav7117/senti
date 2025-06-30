from flask import Flask, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head>
        <title>Sentiment Analyzer with Music</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f0f2f5;
                text-align: center;
                padding-top: 50px;
            }
            input[type="text"] {
                padding: 10px;
                width: 300px;
                border-radius: 5px;
                border: 1px solid #ccc;
                font-size: 16px;
            }
            button {
                padding: 10px 20px;
                font-size: 16px;
                border: none;
                border-radius: 5px;
                background-color: #28a745;
                color: white;
                cursor: pointer;
                margin-left: 10px;
            }
            button:hover {
                background-color: #218838;
            }
        </style>
    </head>
    <body>
        <h2>🎧 Sentiment Analyzer with Mood Music</h2>
        <form method="POST" action="/analyze">
            <input name="text" placeholder="Type something..." required>
            <button type="submit">Analyze</button>
        </form>
    </body>
    </html>
    '''

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    if sentiment > 0:
        mood = "😊 Positive"
        song_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"  # upbeat
    elif sentiment < 0:
        mood = "😞 Negative"
        song_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3"  # calm/sad
    else:
        mood = "😐 Neutral"
        song_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3"  # chill

    return f'''
    <html>
    <head>
        <title>Result with Music</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                text-align: center;
                padding-top: 40px;
            }}
            audio {{
                margin-top: 20px;
            }}
            a {{
                display: inline-block;
                margin-top: 30px;
                padding: 10px 20px;
                background: #28a745;
                color: white;
                text-decoration: none;
                border-radius: 5px;
            }}
            a:hover {{
                background: #218838;
            }}
        </style>
    </head>
    <body>
        <h2>Sentiment: {mood}</h2>
        <p><strong>Score:</strong> {sentiment}</p>
        <p><strong>You wrote:</strong> "{text}"</p>
        <audio controls autoplay>
            <source src="{song_url}" type="audio/mpeg">
            Your browser does not support the audio element.
        </audio>
        <br><br>
        <a href="/">Analyze Another</a>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)

