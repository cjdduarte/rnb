from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate')
def generate_number():
    max_range = int(request.args.get('range', 100))
    number = random.randint(1, max_range)
    return jsonify(str(number))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
