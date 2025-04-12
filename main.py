from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'message': 'Welcome to Grillgorithm! Your smart cooking assistant is alive 🍳✨'
    })

if __name__ == '__main__':
    app.run(debug=True)