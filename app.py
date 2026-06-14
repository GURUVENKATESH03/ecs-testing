from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({
        "status": "success",
        "message": "Hello from inside the Docker container!"
    })

if __name__ == '__main__':
    # '0.0.0.0' is required for Docker to expose the app properly
    app.run(host='0.0.0.0', port=5000)
