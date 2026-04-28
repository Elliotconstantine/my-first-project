from flask import Flask, jsonify
from flask_cors import CORS  # <--- 1. 引入 CORS

app = Flask(__name__)
CORS(app)  # <--- 2. 启用 CORS，给后端装上“通行证”

@app.route('/api/hello')
def hello():
    return jsonify({"message": "你好，我是 Python 后端", "status": "success"})

if __name__ == '__main__':
    app.run(port=5000)