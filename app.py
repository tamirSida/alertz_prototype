from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simulate_attack', methods=['POST'])
def simulate_attack():
    alert_data = {
        "message": "Missile alert! Seek shelter immediately.",
        "shelter": "Nearest shelter: 123 Safe St.",
        "countdown": 45  # seconds
    }
    return jsonify(alert_data)

@app.route('/check_status', methods=['POST'])
def check_status():
    status_data = {
        "message": "Are you safe?",
        "safe": True  # For now, we'll just return True. Implement logic as needed.
    }
    return jsonify(status_data)

if __name__ == '__main__':
    app.run(debug=True)
