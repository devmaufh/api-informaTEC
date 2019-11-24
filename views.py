from run import app
from flask import jsonify
from flask import send_from_directory
@app.route('/')
def index():
    return jsonify({'message': 'Quionda que pex jsjsjs!'})

@app.route('/images/<path:filename>')
def images(filename):
    return send_from_directory('images',filename)
