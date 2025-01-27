from flask import Flask, send_file, jsonify
import os

app = Flask(__name__, static_folder = "static")

@app.route("/", methods=['GET'])
def get_index():
   try:
       return send_file("index.html")
   except FileNotFoundError:
       return jsonify({"error": "HTML file not found"}), 404
   
@app.route("/reg.html", methods=['GET'])
def get_reg():
   try:
       return send_file("reg.html")
   except FileNotFoundError:
       return jsonify({"error": "HTML file not found"}), 404
   
@app.route("/cab.html", methods=['GET'])
def get_cab():
   try:
       return send_file("cab.html")
   except FileNotFoundError:
       return jsonify({"error": "HTML file not found"}), 404

@app.route("/endreg.html", methods=['GET'])
def get_endreg():
   try:
       return send_file("endreg.html")
   except FileNotFoundError:
       return jsonify({"error": "HTML file not found"}), 404
   
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 8000)